"""
WSGI config for Configatron_API project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
sys.path.insert(0, '/var/www/Configatron_API')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Configatron_API.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
