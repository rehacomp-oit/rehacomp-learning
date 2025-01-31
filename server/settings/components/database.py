'''Database configuration for the project'''

from server.settings.components import env_config



# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env_config('POSTGRES_DB'),
        'USER': env_config('POSTGRES_USER'),
        'PASSWORD': env_config('POSTGRES_PASSWORD'),
        'HOST': env_config('DJANGO_DATABASE_HOST'),
        'PORT': env_config('DJANGO_DATABASE_PORT', default=5432, cast=int),
        'CONN_MAX_AGE': env_config('CONN_MAX_AGE', cast=int, default=60),
        'OPTIONS': {
            'connect_timeout': 10,
            'options': '-c statement_timeout=15000ms',
        },
    },
}


MIGRATION_MODULES = {'accounts': 'server.apps.accounts.infrastructure.migrations'}
