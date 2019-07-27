# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=36)),
            ],
            options={
                'verbose_name': '作者',
                'verbose_name_plural': '作者',
                'db_table': 'df_author',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('origkey', models.CharField(max_length=36, blank=True, null=True)),
                ('title', models.TextField()),
                ('year_published', models.DateField(blank=True, null=True)),
                ('comment', models.TextField(blank=True)),
                ('authors', models.ManyToManyField(to='library.Author')),
            ],
            options={
                'verbose_name': '书名',
                'verbose_name_plural': '书名',
                'db_table': 'df_book',
                'ordering': ('year_published', 'title'),
            },
        ),
    ]
