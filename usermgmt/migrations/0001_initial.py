# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 19:50
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
                ('notification_type', models.CharField(choices=[('W', 'Watch'), ('M', 'Message'), ('F', 'Favorite'), ('R', 'Rating'), ('E', 'Enjoy'), ('S', 'Submission comment'), ('C', 'Comment reply'), ('P', 'Promote'), ('H', 'Highlight')], max_length=1)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('subject_id', models.PositiveIntegerField(blank=True, null=True)),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_source', to=settings.AUTH_USER_MODEL)),
                ('subject_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-ctime'],
            },
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
                ('expired_notifications', models.PositiveIntegerField(default=0)),
                ('blocked_users', models.ManyToManyField(related_name='blocked_by', to=settings.AUTH_USER_MODEL)),
                ('favorited_submissions', models.ManyToManyField(related_name='favorited_by', to='submissions.Submission')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_groups', models.ManyToManyField(to='auth.Group')),
                ('watched_users', models.ManyToManyField(related_name='watched_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
