# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20190819_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='group',
            field=models.ForeignKey(null=True, related_name='notes', to='notes.Group',on_delete=models.CASCADE)),
    ]
