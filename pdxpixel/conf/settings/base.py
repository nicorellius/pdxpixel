"""
Django settings for pdxpixel project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(*_DIR, ...)
import environ  # https://github.com/joke2k/django-environ

from django.core.urlresolvers import reverse_lazy

from core.logging import LOGGING_MODULE


# /home/nick/dev/django/projects/pdxpixel
PROJECT_DIR = environ.Path(__file__) - 4

# /home/nick/dev/django/projects/pdxpixel/pdxpixel
SITE_DIR = environ.Path(__file__) - 3

# /home/nick/dev/django/projects/pdxpixel/pdxpixel/conf
CONF_DIR = environ.Path(__file__) - 2

# /home/nick/dev/django/projects/pdxpixel/pdxpixel/conf/settings
SETTINGS_DIR = environ.Path(__file__) - 1

SITE_ID = 1

DEBUG = True

APPEND_SLASH = False

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(SITE_DIR.path('templates'))
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages'
            ],
            'debug': True
        }
    }
]

INSTALLED_APPS = [
    'apps.accounts',
    'core.signals',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'pagedown',
    'markdown_deux',
    'taggit',
    'taggit_templatetags2',
    'watson',
    'bootstrapform',
    'apps.blog',
    'apps.search',
    'core',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'conf.urls'

# WSGI_APPLICATION = 'pdxpixel.conf.wsgi.local'

with open('/etc/prv/pdxpixel/db_password.txt') as db_password:
    DB_PASSWORD = db_password.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pdxpixel',
        'USER': 'pdxpixel',
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
        'PORT': '',
    }
}

# LOGIN_REDIRECT_URL = reverse_lazy('accounts:dashboard')
LOGIN_REDIRECT_URL = reverse_lazy('accounts:profile')
LOGIN_URL = reverse_lazy('accounts:login')
LOGOUT_URL = reverse_lazy('accounts:logout')

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    # str(SITE_DIR.path('apps/blog/static')),
    str(SITE_DIR.path('static')),
)

LOGGING = LOGGING_MODULE

MARKDOWN_DEUX_STYLES = {
    'default': {
        'extras': {
            'code-friendly': None,
        },
        'safe_mode': False,
    },
}
