from django.contrib.sites.models import Site
from hashlib import md5


def get_md5(str):
    m = md5(str.encode('utf-8'))
    return m.hexdigest()


def get_current_site():
    site = Site.objects.get_current()
    return site


def send_email(emailto, title, content):
    from arryblog.signals import send_email_signal
    send_email_signal.send(send_email.__class__, emailto=emailto, title=title, content=content)
