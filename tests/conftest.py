'''
This module is used to provide configuration, fixtures, and plugins for pytest.
'''

pytest_plugins = (
    'plugins.django_settings',
    'plugins.accounts_fixtures',
    'plugins.common_fixtures',
)
