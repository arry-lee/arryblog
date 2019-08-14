# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('content', models.TextField(verbose_name='笔记内容', blank=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('owner', models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '笔记',
                'verbose_name_plural': '笔记',
                'db_table': 'df_note',
            },
        ),
    ]
