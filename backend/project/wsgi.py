# pylint: skip-file
"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import environ

project_root = environ.Path(__file__) - 3
env = environ.Env(DJANGO_SETTINGS_MODULE=(str, ''))
environ.Env.read_env(project_root('.env'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.prod")

application = get_wsgi_application()
