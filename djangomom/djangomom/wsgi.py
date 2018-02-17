"""
WSGI config for djangomom project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from djangomom.settings.base import BASE_DIR
import sys
THIRD_PARTY_APPS_DIR = os.path.normpath(os.path.join(
    BASE_DIR, '../', '../', 'project_directory'))
sys.path += [THIRD_PARTY_APPS_DIR] 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangomom.settings.live")

application = get_wsgi_application()
