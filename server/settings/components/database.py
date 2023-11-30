'''Database configuration for the project'''

from server.settings.components import BASE_DIR


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.joinpath('db.sqlite3'),
    },
}
