'''
This is a django-split-settings main file.

For more information read this:
https://github.com/sobolevn/django-split-settings
https://sobolevn.me/2017/04/managing-djangos-settings

To change settings file:
`DJANGO_ENV=production python manage.py runserver`
'''

from os import environ

from split_settings.tools import include


# Managing environment via `DJANGO_ENV` variable:
environ.setdefault('DJANGO_ENV', 'development')
_current_env = environ['DJANGO_ENV']


_base_settings = (
    'components/caches.py',
    'components/common.py',
    'components/csp.py',
    'components/database.py',
    'components/logging.py',
    'components/ui.py',
    # Select the right env:
    'environments/{0}.py'.format(_current_env),
)

include(*_base_settings)
