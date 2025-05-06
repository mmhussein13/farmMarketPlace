"""
WSGI config for farm_ecommerce project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_ecommerce.settings')

application = get_wsgi_application()
