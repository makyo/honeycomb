# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('usermgmt', '0005_auto_20161111_0247'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='blocked_tags',
            field=models.ManyToManyField(related_name='blocked_by', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='profile',
            name='favorite_tags',
            field=models.ManyToManyField(related_name='favorited_by', to='taggit.Tag'),
        ),
    ]
