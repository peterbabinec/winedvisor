"""
WSGI config for winedvisor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For mor information on this file, seee
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "winedvisor.settings")

application = get_wsgi_application()
