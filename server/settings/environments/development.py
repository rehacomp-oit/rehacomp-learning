'''This file contains all the settings that defines the development server.'''

from __future__ import annotations

import logging
import socket
from typing import TYPE_CHECKING

from server.settings.components.common import INSTALLED_APPS, MIDDLEWARE
from server.settings.components.csp import (
    CSP_CONNECT_SRC,
    CSP_IMG_SRC,
    CSP_SCRIPT_SRC,
)
from server.settings.components.database import DATABASES

if TYPE_CHECKING:
    from django.http import HttpRequest


# Setting the development status:
DEBUG = True

ALLOWED_HOSTS = (
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
    '[::1]',
)


# Installed apps for development only:
INSTALLED_APPS += (
    # Better debug:
    'debug_toolbar',
    'nplusone.ext.django',
    # django-query-counter:
    'query_counter',
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'query_counter.middleware.DjangoQueryCounterMiddleware',
)

# https://django-debug-toolbar.readthedocs.io/en/stable/installation.html#configure-internal-ips
# This might fail on some OS
try:
    INTERNAL_IPS = [
        '{0}.1'.format(ip[:ip.rfind('.')])
        for ip in socket.gethostbyname_ex(socket.gethostname())[2]
    ]
except socket.error:
    INTERNAL_IPS = []

INTERNAL_IPS += ['127.0.0.1', '10.0.2.2']


def _custom_show_toolbar(request: HttpRequest) -> bool:
    '''Only show the debug toolbar to users with the superuser flag.'''
    return DEBUG and request.user.is_superuser


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK':
        'server.settings.environments.development._custom_show_toolbar',
}

# This will make debug toolbar to work with django-csp:
CSP_SCRIPT_SRC += ('ajax.googleapis.com',)
CSP_IMG_SRC += ('data:',)
CSP_CONNECT_SRC += ("'self'",)


# nplusone
# Should be the first in line:
MIDDLEWARE = ('nplusone.ext.django.NPlusOneMiddleware',) + MIDDLEWARE

# Logging N+1 requests:
NPLUSONE_RAISE = True  # comment out if you want to allow N+1 requests
NPLUSONE_LOGGER = logging.getLogger('django')
NPLUSONE_LOG_LEVEL = logging.WARN
NPLUSONE_WHITELIST = [{'model': 'admin.*'},]


# django-test-migrations
# Set of badly named migrations to ignore:
DTM_IGNORED_MIGRATIONS = frozenset((('axes', '*'),))


# django-migration-linter
MIGRATION_LINTER_OPTIONS = {
    'exclude_apps': ['axes'],
    'exclude_migration_tests': ['CREATE_INDEX', 'CREATE_INDEX_EXCLUSIVE'],
    'warnings_as_errors': True,
}


# Disable persistent DB connections
# https://docs.djangoproject.com/en/4.2/ref/databases/#caveats
DATABASES['default']['CONN_MAX_AGE'] = 0
