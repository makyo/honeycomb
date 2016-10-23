# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 04:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('slug', models.SlugField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FolderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submissions.Folder')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('slug', models.SlugField()),
                ('description_raw', models.TextField(blank=True, verbose_name='description')),
                ('description_rendered', models.TextField(blank=True)),
                ('content_raw', models.TextField(blank=True, verbose_name='submission')),
                ('content_rendered', models.TextField()),
                ('content_file', models.FileField(blank=True, upload_to=b'')),
                ('icon', models.ImageField(blank=True, upload_to=b'')),
                ('cover', models.ImageField(blank=True, upload_to=b'')),
                ('can_comment', models.BooleanField(default=True, verbose_name='allow comments')),
                ('can_enjoy', models.BooleanField(default=True, verbose_name='allow enjoy votes')),
                ('adult_rating', models.BooleanField(default=False, verbose_name='submission for adults only')),
                ('hidden', models.BooleanField(default=False)),
                ('restricted_to_groups', models.BooleanField(default=False, verbose_name='restrict visibility to certain groups')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('mtime', models.DateTimeField(auto_now=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('enjoy_votes', models.PositiveIntegerField(default=0)),
                ('allowed_groups', models.ManyToManyField(blank=True, to='auth.Group')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='folderitem',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submissions.Submission'),
        ),
    ]
