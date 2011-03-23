# Django settings for odm project.
import os
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

import socket
HOST_NAME = socket.gethostname()

SITE_LOCAL = SITE_NERSC = False
if HOST_NAME.startswith('sgn'):
    SITE_NERSC = True
else:
    SITE_LOCAL = True

if SITE_NERSC:
    DEBUG = TEMPLATE_DEBUG = False
    SITE_ROOT = '/dayabay/odm'
    MEDIA_URL = 'http://portal.nersc.gov/project/dayabay/odm_media/'
    ADMIN_MEDIA_PREFIX = 'http://portal.nersc.gov/project/dayabay/odm_media/admin/'
    # LOGIN_URL = SITE_ROOT + '/accounts/login'

elif SITE_LOCAL:
    DEBUG = TEMPLATE_DEBUG = True
    SITE_ROOT = ''
    MEDIA_URL = '/media/'
    ADMIN_MEDIA_PREFIX = '/media/admin/'
    
DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',
        'NAME': PROJECT_PATH + '/db/odm.db',          
        'USER': '',          
        'PASSWORD': '',      
        'HOST': '',          
        'PORT': '',          
    }
}

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

ADMINS = (
    ('Chao Zhang', 'chao.zh@gmail.com'),
)
MANAGERS = ADMINS

ROOT_URLCONF = 'odm.urls'
SECRET_KEY = ')x6%ue!mjwlw3u)t3wxtc%hktov$ti!w@%v1n)q72-$%6g*kp9'
TIME_ZONE = 'America/Los Angeles'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)


TEMPLATE_DIRS = (
    # Always use forward slashes, even on Windows.
    PROJECT_PATH + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
)

SESSION_COOKIE_AGE = 86400 * 3
