import json
import requests
from hashlib import md5

from django.contrib.sites.models import Site

def get_md5(str):
    m = md5(str.encode('utf-8'))
    return m.hexdigest()


def get_current_site():
    site = Site.objects.get_current()
    return site


def send_email(emailto, title, content):
    from arryblog.signals import send_email_signal
    send_email_signal.send(send_email.__class__, emailto=emailto, title=title, content=content)


def get_quote(date = '2018-10-30'):
	url = 'https://rest.shanbay.com/api/v2/quote/quotes/%s/'% date
	response = requests.get(url,verify=False)
	quotes_dict = json.loads(response.text)
	return( quotes_dict['data']['content'],quotes_dict['data']['translation'],quotes_dict['data']['author'])