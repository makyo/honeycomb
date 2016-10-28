from __future__ import unicode_literals
import markdown

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.html import strip_tags

from honeycomb_markdown import HoneycombMarkdown
from usermgmt.group_models import FriendGroup


class Submission(models.Model):
    # Submission owner
    owner = models.ForeignKey(User)

    # Title and slug generated from title
    title = models.CharField(max_length=1000)
    slug = models.SlugField()

    # Content written by the user
    description_raw = models.TextField(blank=True, verbose_name="description")
    description_rendered = models.TextField(blank=True)
    content_raw = models.TextField(blank=True, verbose_name="submission")
    content_rendered = models.TextField()
    content_file = models.FileField(blank=True)

    # Associated images
    icon = models.ImageField(blank=True)
    cover = models.ImageField(blank=True)

    # Flags
    can_comment = models.BooleanField(
        default=True,
        verbose_name='allow comments')
    can_enjoy = models.BooleanField(
        default=True,
        verbose_name='allow enjoy votes')
    adult_rating = models.BooleanField(
        default=False,
        verbose_name='submission for adults only')
    hidden = models.BooleanField(default=False)
    allowed_groups = models.ManyToManyField(FriendGroup, blank=True)

    # Organization
    restricted_to_groups = models.BooleanField(
        default=False,
        verbose_name='restrict visibility to certain groups')
    folders = models.ManyToManyField('Folder', through='FolderItem',
                                     blank=True)

    # Additional metadata
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    enjoy_votes = models.PositiveIntegerField(default=0)
    rating_stars = models.CharField(max_length=40, default='&#x2606;' * 5)
    rating_average = models.DecimalField(max_digits=3, decimal_places=2,
                                         default=0.0)
    rating_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.description_rendered = markdown.markdown(
            strip_tags(self.description_raw),
            extensions=['pymdownx.extra', HoneycombMarkdown()])
        self.content_rendered = markdown.markdown(
            strip_tags(self.content_raw),
            extensions=['pymdownx.extra', HoneycombMarkdown()])
        super(Submission, self).save(*args, **kwargs)

    def get_average_rating(self):
        total = count = 0
        for rating in self.rating_set.all():
            total += rating.rating
            count += 1
        if count > 0:
            return {
                'stars': '&#x2605;' * int(total / count) +
                         '&#x2606;' * (5 - int(total / count)),
                'average': float(total) / float(count),
                'count': count
            }
        else:
            return {'stars': '', 'average': 0, 'count': 0}

    def __str__(self):
        return '{} by {} (id:{})'.format(self.title, self.owner.username,
                                         self.id)

    def __unicode__(self):
        return '{} by {} (id:{})'.format(self.title, self.owner.username,
                                         self.id)


class Folder(models.Model):
    # Folder owner
    owner = models.ForeignKey(User)

    # Parent folder
    parent = models.ForeignKey('Folder', blank=True, null=True)

    # Folder name and slug generated from name
    name = models.CharField(max_length=1000)
    slug = models.SlugField()

    submissions = models.ManyToManyField(Submission, through='FolderItem')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Folder, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class FolderItem(models.Model):
    # Submission and folder relations
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

    # Position in ordering
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ['position']
