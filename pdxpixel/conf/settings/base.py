"""
Django settings for pdxpixel project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(*_DIR, ...)
import environ  # https://github.com/joke2k/django-environ

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
                "django.contrib.auth.context_processors.auth",
            ],
            'debug': True
        }
    }
]

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
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
    'apps.blog',
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

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

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

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# static files
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    str(SITE_DIR.path('apps/blog/static')),
    str(SITE_DIR.path('static')),
)

