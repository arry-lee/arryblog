# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190724_0254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='source',
        ),
    ]
