import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mutts.settings")

app = get_wsgi_application()  # Change `application` to `app` for Vercel
