# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 02:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('submissions', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(max_length=1)),
                ('subject_id', models.PositiveIntegerField()),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_source', to=settings.AUTH_USER_MODEL)),
                ('subject_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=100)),
                ('profile_raw', models.TextField(blank=True, verbose_name='profile text')),
                ('profile_rendered', models.TextField(blank=True)),
                ('attributes', models.TextField(blank=True)),
                ('can_see_adult_submissions', models.BooleanField(default=True)),
                ('results_per_page', models.PositiveIntegerField(default=25)),
                ('blocked_users', models.ManyToManyField(related_name='blocked_by', to=settings.AUTH_USER_MODEL)),
                ('favorited_submissions', models.ManyToManyField(to='submissions.Submission')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_groups', models.ManyToManyField(to='auth.Group')),
                ('watched_users', models.ManyToManyField(related_name='watched_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
