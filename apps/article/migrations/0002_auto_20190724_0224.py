# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)),
        
        migrations.AddField(
            model_name='articleimage',
            name='article',
            field=models.ForeignKey(verbose_name='所属文章', to='article.Article',on_delete=models.CASCADE)),
        
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(verbose_name='标签集', to='article.Tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.ForeignKey(verbose_name='文章类型', to='article.ArticleType',on_delete=models.CASCADE)),
        
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)),
        
    ]
