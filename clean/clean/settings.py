# -*- coding: utf-8 -*-
"""
Django settings for clean project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'clientes',
    'medicao',
    'clean',
]

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/admin/'

AUTH_USER_MODEL = 'accounts.User'
 

try:
  from local_settings import *
except ImportError:
  pass