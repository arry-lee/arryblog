from django.db import models
# Create your models here.

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    '''代码片段模型'''
    question = models.CharField(max_length=40, default='这段代码输出是什么？',verbose_name='题目')
    code = models.TextField(verbose_name='代码段')
    output = models.CharField(max_length=40, null=True,verbose_name='输出')
    reason = models.CharField(max_length=200, null=True,verbose_name='解释')

    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python3', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        db_table = 'df_snippet'
        verbose_name = '代码段'
        verbose_name_plural = verbose_name