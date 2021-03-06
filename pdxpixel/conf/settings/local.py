from .base import *

DEBUG = True

# secret key for development -- used sequence generated by Django
with open('/etc/prv/pdxpixel/secret_key.txt') as secret_key:
    SECRET_KEY = secret_key.read().strip()

INSTALLED_APPS += (
    'debug_toolbar',
)
