from pygments import highlight 
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter 
from pygments.util import ClassNotFound 
from django.utils.safestring import mark_safe
from django import template
import re

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
		return highlight(code, lexer, formatter).decode('utf-8') 
	else: 
		return code

@register.filter
def getlines(data,n=6): 
	"""文章摘要过滤器"""
	# 按句点和换行符分割 返回前n句(非空)
	n = int(n)
	if n <= 0:
		raise ValueError('Negative Lines')

	line = re.split(r'[,。，；？\n]+',data,n)
	# 单句过长则减少行数
	return mark_safe('<br>'.join(line[:n]))
