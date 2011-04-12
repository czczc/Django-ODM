# Django settings for odm project.
import os
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

import socket
HOST_NAME = socket.gethostname()

from ConfigParser import SafeConfigParser
conf = SafeConfigParser()
conf.read(os.path.join(PROJECT_PATH, 'odm.conf'))

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
        'ENGINE'  : 'sqlite3',
        'NAME'    : PROJECT_PATH + conf.get('default_db', 'NAME'),          
        'USER'    : '',          
        'PASSWORD': '',      
        'HOST'    : '',          
        'PORT'    : '',          
    },
    'lbl' : {
        'ENGINE'  : 'mysql',
        'NAME'    : conf.get('lbl_db', 'NAME'),
        'USER'    : conf.get('lbl_db', 'USER'),
        'PASSWORD': conf.get('lbl_db', 'PASSWORD'),
        'HOST'    : conf.get('lbl_db', 'HOST'),
    },
}
DATABASE_ROUTERS = ['odm.router.DayaBayOfflineRouter', 'odm.router.LocalRouter']

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

ADMINS = (
    ('Chao Zhang', 'chao.zh@gmail.com'),
)
MANAGERS = ADMINS

ROOT_URLCONF = 'odm.urls'
SECRET_KEY = conf.get('common', 'SECRET_KEY')
TIME_ZONE = 'America/Los Angeles'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = False
DATETIME_FORMAT = 'Y-m-d H:i:s' 


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

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'odm.context_processors.setting',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'registration',
    'odm.templatelib',
    # 'odm.runinfo',
)

SESSION_COOKIE_AGE = 86400 * 3
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_URL = SITE_ROOT + '/accounts/login'
LOGIN_REDIRECT_URL = SITE_ROOT + '/run/'
LOGOUT_URL = SITE_ROOT + '/accounts/logout'

VERSION = '0.9'
