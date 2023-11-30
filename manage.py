#!/usr/bin/env python
'''Django's command-line utility for running administrative tasks.'''

import os
import sys
from typing import Final


ERROR_MESSAGE: Final = 'Couldn\'t import Django. '\
    'Are you sure it\'s installed and '\
    'available on your PYTHONPATH environment variable? Did you '\
    'forget to activate a virtual environment?'


def main() -> None:
    '''
    Main function.

    It does several things:
    1. Sets default settings module, if it is not set
    2. Warns if Django is not installed
    3. Executes any given command
    '''
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError(ERROR_MESSAGE)
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
