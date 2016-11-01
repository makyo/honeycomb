# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 06:25
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0005_submission_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]