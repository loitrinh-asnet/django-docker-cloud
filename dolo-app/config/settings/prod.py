"""Prod settings for dolo-app project."""

from .base import *  # noqa

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['localhost', ])

SECRET_KEY = env('DJANGO_SECRET_KEY', default='y7Fxywd1JpgR9dY&^<Nl5SDL@u2L4@11(,8hQaH;>wtUIoClzU')

INSTALLED_APPS += ['gunicorn', ]
