# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0009_auto_20161109_0428'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ban',
            options={'ordering': ('-start_date',), 'permissions': (('can_ban_users', 'Can ban users'), ('can_list_bans', 'Can list bans'), ('can_view_bans', 'Can view bans'), ('can_lift_bans', 'Can lift bans'))},
        ),
        migrations.AddField(
            model_name='ban',
            name='user_has_viewed',
            field=models.BooleanField(default=False),
        ),
    ]
