# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 07:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activitystream', '0004_auto_20161030_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
