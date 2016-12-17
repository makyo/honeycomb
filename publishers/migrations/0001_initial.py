# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 22:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import publishers.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('submitify', '0005_auto_20161204_0003'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('mtime', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to=publishers.models.newsitem_path)),
                ('subject', models.CharField(max_length=200)),
                ('body_raw', models.TextField(verbose_name='body')),
                ('body_rendered', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('url', models.URLField(max_length=1024)),
                ('logo', models.ImageField(upload_to=publishers.models.logo_path)),
                ('banner', models.ImageField(blank=True, upload_to=publishers.models.banner_path)),
                ('body_raw', models.TextField(verbose_name='body')),
                ('body_rendered', models.TextField()),
                ('calls', models.ManyToManyField(to='submitify.Call')),
                ('editors', models.ManyToManyField(related_name='publisher_editor_of', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='publisher_member_of', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_publisher_page', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='newsitem',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publishers.Publisher'),
        ),
    ]
