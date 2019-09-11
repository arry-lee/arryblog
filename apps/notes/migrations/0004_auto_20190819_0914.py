# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20190819_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, related_name='children', to='notes.Group',on_delete=models.CASCADE)),
    ]
