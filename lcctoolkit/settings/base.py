"""
Django settings for lcctoolkit project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import environ
import os
from datetime import datetime

env = environ.Env(DEBUG=(bool, False),)
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_elasticsearch_dsl',
    'rolepermissions',
    'rest_framework',
    'mptt',
    'captcha',
    'lcc'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'lcc.middleware.user_profile'
]

ROOT_URLCONF = 'lcctoolkit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'lcc.context.sentry',
                'lcc.context.ga_tracking_id',
            ]
        },
    },
]

WSGI_APPLICATION = 'lcctoolkit.wsgi.application'
ROLEPERMISSIONS_MODULE = 'lcc.roles'


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = "/login/"

FIXTURE_DIRS = [
    'lcc/tests/fixtures',
]

DOCS_ROOT = os.path.join(BASE_DIR, '..', 'docs/_build/html')

LAWS_PER_PAGE = 10

# Used to concatenate classification and tag names in ES indexes
TAXONOMY_CONNECTOR = '; '

MIN_YEAR = 1945

MAX_YEAR = datetime.now().year

# File upload

FILE_UPLOAD_PERMISSIONS = 0o644

LEGISPRO_URL=env('LEGISPRO_URL')
UNHABITAT_URL=env('UNHABITAT_URL')
UNFAO_URL=env('UNFAO_URL')
LEGISPRO_USER=env('LEGISPRO_USER')
LEGISPRO_PASS=env('LEGISPRO_PASS')
