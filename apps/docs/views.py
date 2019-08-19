import inspect
import os
import re
from importlib import import_module

from django.apps import apps
from django.conf import settings
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.admindocs import utils
from django.core import urlresolvers
from django.core.exceptions import ImproperlyConfigured, ViewDoesNotExist
from django.db import models
from django.http import Http404
from django.template.base import (
    InvalidTemplateLibrary, builtins, get_library, get_templatetags_modules,
    libraries,
)
from django.template.engine import Engine
from django.utils import six
from django.utils._os import upath
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView
from django.utils.safestring import mark_safe

# Exclude methods starting with these strings from documentation
MODEL_METHODS_EXCLUDE = ('_', 'add_', 'delete', 'save', 'set_')

APP_LABEL_EXCLUDE = ('admin','auth','contenttypes','sessions','library','django_comments')

APP_LABEL_INCLUDE = ('user','article','photo','card','notes','docs')


class ModelIndexView(TemplateView):
    template_name = 'djangodoc.md'

    def get_context_data(self, **kwargs):
        m_list = []
        for model in apps.get_models():
            opts = model._meta
            if opts.app_label not in APP_LABEL_INCLUDE:
                continue
            title, body, metadata = utils.parse_docstring(model.__doc__)
            if title:
                title = utils.parse_rst(title, 'model', _('model:') + opts.model_name)
            if body:
                body = utils.parse_rst(body, 'model', _('model:') + opts.model_name)

            # Gather fields/field descriptions.
            fields = []
            for field in opts.fields:
                # ForeignKey is a special case since the field will actually be a
                # descriptor that returns the other object
                if isinstance(field, models.ForeignKey):
                    data_type = field.rel.to.__name__
                    app_label = field.rel.to._meta.app_label
                    verbose = mark_safe(_("the related <a href='#%(app_label)s.%(data_type)s'>%(app_label)s.%(data_type)s</a> object") % {
                            'app_label': app_label, 'data_type': data_type,})
                else:
                    data_type = get_readable_field_data_type(field)
                    verbose = field.verbose_name
                fields.append({
                    'name': field.name,
                    'data_type': data_type,
                    'verbose': verbose,
                    'help_text': field.help_text,
                })

            # Gather many-to-many fields.
            for field in opts.many_to_many:
                data_type = field.rel.to.__name__
                app_label = field.rel.to._meta.app_label
                verbose = "the related <a href='#%(app_label)s.%(data_type)s'>%(app_label)s.%(data_type)s</a> object"% {
                            'app_label': app_label, 'data_type': data_type,}

                fields.append({
                    'name': "%s.all" % field.name,
                    "data_type": 'List',
                    'verbose': mark_safe(_("all %s" % verbose))
                })

                fields.append({
                    'name': "%s.count" % field.name,
                    'data_type': 'Integer',
                    'verbose':mark_safe(_("number of %s"% verbose))
                })

            # Gather model methods.
            for func_name, func in model.__dict__.items():
                if (inspect.isfunction(func) and len(inspect.getargspec(func)[0]) == 1):
                    try:
                        for exclude in MODEL_METHODS_EXCLUDE:
                            if func_name.startswith(exclude):
                                raise StopIteration
                    except StopIteration:
                        continue
                    verbose = func.__doc__
                    if verbose:
                        verbose = utils.parse_rst(utils.trim_docstring(verbose), 'model', _('model:') + opts.model_name)
                    fields.append({
                        'name': func_name,
                        'data_type': get_return_data_type(func_name),
                        'verbose': verbose,
                    })

            # Gather related objects
            for rel in opts.related_objects:
                verbose = "related <a href='#%(app_label)s.%(object_name)s'>%(app_label)s.%(object_name)s</a> objects"% {
                    'app_label': rel.related_model._meta.app_label,
                    'object_name': rel.related_model._meta.object_name,
                }
                accessor = rel.get_accessor_name()
                fields.append({
                    'name': "%s.all" % accessor,
                    'data_type': 'List',
                    'verbose': mark_safe(_("all %s"% verbose)),
                })
                fields.append({
                    'name': "%s.count" % accessor,
                    'data_type': 'Integer',
                    'verbose': mark_safe(_("number of %s"% verbose)),
                })

            d = {
                'name': '%s.%s' % (opts.app_label, opts.object_name),
                'summary': title,
                'description': body,
                'fields': fields,}

            m_list.append(d)
        kwargs.update({
            'models': m_list
        })
        return super().get_context_data(**kwargs)

####################
# Helper functions #
####################

def load_all_installed_template_libraries():
    # Load/register all template tag libraries from installed apps.
    for module_name in get_templatetags_modules():
        mod = import_module(module_name)
        if not hasattr(mod, '__file__'):
            # e.g. packages installed as eggs
            continue

        try:
            libraries = [
                os.path.splitext(p)[0]
                for p in os.listdir(os.path.dirname(upath(mod.__file__)))
                if p.endswith('.py') and p[0].isalpha()
            ]
        except OSError:
            continue
        else:
            for library_name in libraries:
                try:
                    get_library(library_name)
                except InvalidTemplateLibrary:
                    pass


def get_return_data_type(func_name):
    """Return a somewhat-helpful data type given a function name"""
    if func_name.startswith('get_'):
        if func_name.endswith('_list'):
            return 'List'
        elif func_name.endswith('_count'):
            return 'Integer'
    return ''


def get_readable_field_data_type(field):
    """Returns the description for a given field type, if it exists,
    Fields' descriptions can contain format strings, which will be interpolated
    against the values of field.__dict__ before being output."""

    return field.description % field.__dict__


def extract_views_from_urlpatterns(urlpatterns, base='', namespace=None):
    """
    Return a list of views from a list of urlpatterns.

    Each object in the returned list is a two-tuple: (view_func, regex)
    """
    views = []
    for p in urlpatterns:
        if hasattr(p, 'url_patterns'):
            try:
                patterns = p.url_patterns
            except ImportError:
                continue
            views.extend(extract_views_from_urlpatterns(
                patterns,
                base + p.regex.pattern,
                (namespace or []) + (p.namespace and [p.namespace] or [])
            ))
        elif hasattr(p, 'callback'):
            try:
                views.append((p.callback, base + p.regex.pattern,
                              namespace, p.name))
            except ViewDoesNotExist:
                continue
        else:
            raise TypeError(_("%s does not appear to be a urlpattern object") % p)
    return views

named_group_matcher = re.compile(r'\(\?P(<\w+>).+?\)')
non_named_group_matcher = re.compile(r'\(.*?\)')


def simplify_regex(pattern):
    """
    Clean up urlpattern regexes into something somewhat readable by Mere Humans:
    turns something like "^(?P<sport_slug>\w+)/athletes/(?P<athlete_slug>\w+)/$"
    into "<sport_slug>/athletes/<athlete_slug>/"
    """
    # handle named groups first
    pattern = named_group_matcher.sub(lambda m: m.group(1), pattern)

    # handle non-named groups
    pattern = non_named_group_matcher.sub("<var>", pattern)

    # clean up any outstanding regex-y characters.
    pattern = pattern.replace('^', '').replace('$', '').replace('?', '').replace('//', '/').replace('\\', '')
    if not pattern.startswith('/'):
        pattern = '/' + pattern
    return pattern
