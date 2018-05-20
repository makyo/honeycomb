"""
Django settings for honeycomb project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from django.contrib import messages
from .revno import *  # noqa: F401,F403

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l0((y2a9+juu5980ft3r_pivfm0#&h3$#zm%(=ulf!lq62+c6%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SITE_ID = 1

ROOT_URLCONF = 'honeycomb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'honeycomb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.' +
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
                'NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'uploads')


# Additional configuration for Honeycomb

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'uploads')

# Installed applications for Honeycomb
INSTALLED_APPS += [
    'core',
    'api',
    'usermgmt',
    'submissions',
    'social',
    'publishers',
    'promotion',
    'activitystream',
    'administration',
    'tags',
    'taggit',
    'submitify',
    'haystack',
    'datetimewidget',
    #'django_extensions',
]
MIDDLEWARE = [
    'honeycomb.middleware.BanMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Caching mechanisms
CACHES = {
    # Enable this backend for no caching.
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
    # Enable this backend for default caching in local memory.
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    #     'LOCATION': 'dev-cache',
    # }
    # TODO production should use memcached
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    #     'LOCATION': '127.0.0.1:11211',
    # }
}

# Search engine connections
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
    # TODO production should use elasticsearch
    # 'default': {
    #     'ENGINE':
    #         ('haystack.backends.elasticsearch_backend.'
    #          'ElasticsearchSearchEngine'),
    #     'URL': 'http://corrin.local:9200/',
    #     'INDEX_NAME': 'honeycomb',
    # },
}

# Make tags case insensitive
TAGGIT_CASE_INSENSITIVE = True

# Base URL pattern for submissions
SUBMISSION_BASE = ('^~(?P<username>[^/]+)/(?P<submission_id>\d+)-'
                   '(?P<submission_slug>[-\w]+)/')

# How often to run various commands through cron
ACTIVITYSTREAM_ROTATION = 1  # Rotation period in days

# Login conventions
LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = LOGIN_URL

# Reset message tags to work with bootstrap
MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# Additional logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
}

# Maximum file upload size
# NB you should also set this up on the server through apache/nginx config;
# this is only intended to be a backup
MAX_UPLOAD_SIZE = 1024 * 1024 * 10

# The content types (in the form app_label:model) which users can flag for
# administrative review.
FLAGGABLE_CONTENT_TYPES = [
    'promotion:adlifecycle',
    'publishers:publisher',
    'social:comment',
    'submissions:submission',
    'taggit:tag',
    'usermgmt:profile',
]
UTM_SOURCE = 'Honeycomb'
