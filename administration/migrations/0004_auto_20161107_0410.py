# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 04:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administration', '0003_auto_20161106_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_type', models.CharField(choices=[('p', 'Create a publisher page'), ('c', 'Claim a publisher'), ('e', 'Schedule an event'), ('a', 'Create an ad'), ('l', 'Schedule an ad lifecycle'), ('s', 'Become a social moderator'), ('m', 'Become a content moderator')], max_length=1)),
                ('body_raw', models.TextField(verbose_name='body')),
                ('body_rendered', models.TextField()),
                ('admin_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications_responsible_for', to=settings.AUTH_USER_MODEL)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('can_list_social_applications', 'Can list social applications'), ('can_view_social_applications', 'Can view social applications'), ('can_resolve_social_applications', 'Can resolve social applications'), ('can_list_content_applications', 'Can list content applications'), ('can_view_content_applications', 'Can view content applications'), ('can_resolve_content_applications', 'Can resolve content applications'), ('can_resolve_applications', 'Can resolve applications')),
            },
        ),
        migrations.AlterModelOptions(
            name='ban',
            options={'permissions': (('can_ban_users', 'Can ban users'), ('can_list_bans', 'Can list bans'), ('can_view_bans', 'Can view bans'), ('can_lift_bans', 'Can lift bans'))},
        ),
        migrations.AlterModelOptions(
            name='flag',
            options={'permissions': (('can_list_social_flags', 'Can list social flags'), ('can_view_social_flags', 'Can view social flags'), ('can_resolve_social_flags', 'Can resolve social flags'), ('can_list_content_flags', 'Can list content flags'), ('can_view_content_flags', 'Can view content flags'), ('can_resolve_content_flags', 'Can resolve content flags'), ('can_resolve_flags', 'Can resolve flags'))},
        ),
        migrations.RenameField(
            model_name='flag',
            old_name='body',
            new_name='body_raw',
        ),
        migrations.AddField(
            model_name='ban',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='flag',
            name='body_rendered',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flag',
            name='flag_type',
            field=models.CharField(choices=[('s', 'Social flags'), ('c', 'Content flags')], default='s', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flag',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='flags_party_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
