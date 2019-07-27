# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190724_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='source',
            field=models.CharField(verbose_name='出处', max_length=200),
        ),
    ]
