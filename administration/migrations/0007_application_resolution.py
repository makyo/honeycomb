# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0006_application_ctime'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='resolution',
            field=models.CharField(blank=True, choices=[('a', 'Accepted'), ('r', 'Rejected')], max_length=1),
        ),
    ]