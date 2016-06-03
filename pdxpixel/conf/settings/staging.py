from .base import *

DEBUG = False

# secret key for staging/development -- used sequence generated by Django
with open('/etc/prv/pdxpixel/secret_key.txt') as secret_key:
    SECRET_KEY = secret_key.read().strip()

STATIC_ROOT = '/var/www/pdxpixel/static'
MEDIA_ROOT = '/var/www/pdxpixel/media'

ALLOWED_HOSTS = ['staging.pdxpixel.com']

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
