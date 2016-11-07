# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0009_auto_20161106_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='description_raw',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='folder',
            name='description_rendered',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='folder',
            name='is_serial',
            field=models.BooleanField(default=False),
        ),
    ]
