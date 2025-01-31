'''
Common django settings for project
'''

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from server.settings.components import BASE_DIR, env_config


SECRET_KEY = env_config('DJANGO_SECRET_KEY')

# Application definition
INSTALLED_APPS: tuple[str, ...] = (
    # Internal apps go here:
    'server.apps.accounts',
    'server.apps.main',
    'server.apps.request_folders',

    # Default django apps:
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ajax:
    'django_htmx',

    # Security:
    'axes',
    'csp',

    # Health checks:
    # see: https://github.com/KristianOellegaard/django-health-check
    'health_check',
    'health_check.db',
    'health_check.cache',
    'health_check.storage',
)


MIDDLEWARE: tuple[str, ...] = (
    # Logging:
    'server.settings.components.logging.LoggingContextVarsMiddleware',

    # Content Security Policy:
    'csp.middleware.CSPMiddleware',

    # Django:
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # django-permissions-policy
    'django_permissions_policy.PermissionsPolicyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_htmx.middleware.HtmxMiddleware',

    # Axes:
    'axes.middleware.AxesMiddleware',

    # Django HTTP Referrer Policy:
    'django_http_referrer_policy.middleware.ReferrerPolicyMiddleware',
)


ROOT_URLCONF = 'server.urls'
WSGI_APPLICATION = 'server.wsgi.application'

# Media files
# Media root dir is commonly changed in production
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Django authentication system
LOGIN_URL = reverse_lazy('accounts:login')
AUTHENTICATION_BACKENDS = (
    'axes.backends.AxesBackend',
    'django.contrib.auth.backends.ModelBackend',
)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
)

AUTH_PASSWORD_VALIDATORS = (
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 9},
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
)


# Internationalization
LANGUAGE_CODE = 'ru-RU'
USE_I18N = True
LANGUAGES = (('ru', _('Russian')),)
LOCALE_PATHS = ('locale/',)
USE_TZ = True
TIME_ZONE = 'Europe/Moscow'


# Security
# https://docs.djangoproject.com/en/4.2/topics/security/
CSRF_COOKIE_HTTPONLY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# https://github.com/DmytroLitvinov/django-http-referrer-policy
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy
REFERRER_POLICY = 'same-origin'

# https://github.com/adamchainz/django-permissions-policy#setting
PERMISSIONS_POLICY: dict[str, str | list[str]] = {}  # noqa: WPS234


# Timeouts
# https://docs.djangoproject.com/en/4.2/ref/settings/#std:setting-EMAIL_TIMEOUT
EMAIL_TIMEOUT = 5


# Session
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_COOKIE_HTTPONLY = True
