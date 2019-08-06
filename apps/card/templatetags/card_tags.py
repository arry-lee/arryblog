from pygments import highlight 
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter 
from pygments.util import ClassNotFound 
from django.utils.safestring import mark_safe
from django import template


register = template.Library()

@register.filter
def highlight_code(code, lang): 
  if code is not None: 
    try: 
      lexer = get_lexer_by_name(lang, encoding='utf-8', stripall=True, startinline=True) 
    except ClassNotFound: 
      lexer = get_lexer_by_name('text') 
    formatter = HtmlFormatter(encoding='utf-8', style='monokai', 
                          linenos=False, cssclass='syntax') 
    return mark_safe(highlight(code, lexer, formatter))   
  else: 
    return mark_safe(code)