'''
This file contains all the settings used in production.
'''

from server.settings.components import env_config as config


# Production flags:
DEBUG = False
ALLOWED_HOSTS = (
    config('DOMAIN_NAME'),
    'localhost',
)


# Staticfiles
_COLLECTSTATIC_DRYRUN = config('DJANGO_COLLECTSTATIC_DRYRUN', cast=bool, default=False)
STATIC_ROOT = '.static' if _COLLECTSTATIC_DRYRUN else '/var/www/django/static'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


# Media files
MEDIA_ROOT = '/var/www/django/media'


# Security
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
# This is required for healthcheck to work:
SECURE_REDIRECT_EXEMPT = ('^health/',)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
