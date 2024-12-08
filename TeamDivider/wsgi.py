"""
WSGI config for TeamDivider project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from waitress import serve
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TeamDivider.settings')

application = get_wsgi_application()

if __name__ == "__main__":
    # Running the application using Waitress on port 8000
    serve(application, host='0.0.0.0', port=8000)
