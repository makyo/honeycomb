# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0007_auto_20161101_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='cover_attribution',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
