# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 21:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20161105_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='social.Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='target_object_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_by_others', to=settings.AUTH_USER_MODEL),
        ),
    ]