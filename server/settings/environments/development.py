'''This file contains all the settings that defines the development server.'''

from server.settings.components.database import DATABASES


# Setting the development status:
DEBUG = True

ALLOWED_HOSTS = (
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
    '[::1]',
)

# Disable persistent DB connections
# https://docs.djangoproject.com/en/4.2/ref/databases/#caveats
DATABASES['default']['CONN_MAX_AGE'] = 0
