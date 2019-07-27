# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('name', models.CharField(verbose_name='相册名称', max_length=20)),
                ('logo', models.CharField(verbose_name='Logo', max_length=20)),
                ('disc', models.CharField(verbose_name='描述', max_length=200)),
                ('thumbnail', models.ImageField(verbose_name='相册缩略图', upload_to='photo')),
            ],
            options={
                'verbose_name': '相册',
                'verbose_name_plural': '相册',
                'db_table': 'df_album',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('image', models.ImageField(verbose_name='原图', upload_to='photo')),
                ('title', models.CharField(verbose_name='照片标题', max_length=40)),
                ('content', models.CharField(verbose_name='照片描述', max_length=200)),
                ('view', models.IntegerField(verbose_name='访问量', default=1)),
                ('like', models.IntegerField(verbose_name='点赞数', default=1)),
                ('type', models.ForeignKey(verbose_name='照片类型', to='photo.Album')),
            ],
            options={
                'verbose_name': '照片',
                'verbose_name_plural': '照片',
                'db_table': 'df_photo',
            },
        ),
    ]
