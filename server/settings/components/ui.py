'''
User interface configuration for the application: static files and templates
'''

from server.settings.components import PROJECT_PACKAGE_DIR


TEMPLATES = ({
    'APP_DIRS': True,
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': (PROJECT_PACKAGE_DIR.joinpath('common', 'django', 'templates'),),
    'OPTIONS': {
        'context_processors': (
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ),
    },
},)


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = (PROJECT_PACKAGE_DIR.joinpath('common', 'django', 'static'),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
