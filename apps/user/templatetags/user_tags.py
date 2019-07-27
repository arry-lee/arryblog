import hashlib
import urllib
from urllib.parse import urlencode
from django import template
from django.utils.safestring import mark_safe
 
register = template.Library()
 
# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
def gravatar_url(email, size=40):
  default = "http://arrylee.com/static/images/arry460.png"
  return "https://www.gravatar.com/avatar/%s?%s" % (hashlib.md5(email.lower().encode("utf8")).hexdigest(), urlencode({'d':default, 's':str(size)}))
 
# return an image tag with the gravatar
# TEMPLATE USE:  {{ email|gravatar:150 }}
@register.filter
def gravatar(email, size=40):
    url = gravatar_url(email, size)
    return mark_safe('<img src="%s" height="%d" width="%d" class="img-thumbnail" />' % (url, size, size))

if __name__ == '__main__':
	a = gravatar_url('me@zezo.com')
	print(a)