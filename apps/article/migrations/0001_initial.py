# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('title', models.CharField(verbose_name='文章标题', max_length=40)),
                ('content', mdeditor.fields.MDTextField(verbose_name='文章内容', blank=True)),
                ('view', models.IntegerField(verbose_name='访问量', default=1)),
                ('like', models.IntegerField(verbose_name='点赞数', default=1)),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 'df_article',
            },
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('image', models.ImageField(verbose_name='图片路径', upload_to='article')),
            ],
            options={
                'verbose_name': '文章图片',
                'verbose_name_plural': '文章图片',
                'db_table': 'df_article_image',
            },
        ),
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('name', models.CharField(verbose_name='种类名称', max_length=20)),
                ('logo', models.CharField(verbose_name='标识', max_length=20)),
            ],
            options={
                'verbose_name': '文章类型',
                'verbose_name_plural': '文章类型',
                'db_table': 'df_article_type',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('content', tinymce.models.HTMLField(verbose_name='评论内容', blank=True)),
                ('article', models.ForeignKey(verbose_name='所评论文章', to='article.Article',on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'db_table': 'df_comment',
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField()),
                ('quote', models.CharField(verbose_name='名言', max_length=200)),
                ('translation', models.CharField(verbose_name='翻译', max_length=200)),
                ('source', models.CharField(verbose_name='出处', max_length=20)),
            ],
            options={
                'verbose_name': '每日一句',
                'verbose_name_plural': '每日一句',
                'db_table': 'df_quote',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('name', models.CharField(verbose_name='标签名称', max_length=20)),
                ('color', models.CharField(verbose_name='颜色', max_length=20)),
            ],
            options={
                'verbose_name': '标签类型',
                'verbose_name_plural': '标签类型',
                'db_table': 'df_tag',
            },
        ),
    ]
