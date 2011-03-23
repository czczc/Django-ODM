import os, sys
sys.stdout = sys.stderr
os.environ["PYTHON_EGG_CACHE"]="/project/projectdirs/dayabay/django-sites/.python-eggs"
path = '/project/projectdirs/dayabay/django-sites'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'odm.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
