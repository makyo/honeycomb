# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_auto_20161106_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ban',
            name='flag',
            field=models.ManyToManyField(blank=True, to='administration.Flag'),
        ),
    ]
