'''
Settings for the logging mechanism of the project
'''


_DEFAULT_MESSAGE_FORMATTER = {
    'format': (
        '%(asctime)s %(levelname)s: '
        '%(message)s [in %(pathname)s'
    )
}


_LOG_HENDLERS = {
    'info_console_handler': {
        'class': 'logging.StreamHandler',
        'formatter': 'default',
        'stream': 'ext://sys.stdout',
    },
    'error_console_handler': {
        'class': 'logging.StreamHandler',
        'formatter': 'default',
        'stream': 'ext://sys.stderr',
    },
}


_LOGGERS = {
    'django': {
        'handlers': ('info_console_handler',),
        'propagate': True,
        'level': 'INFO',
    },
    'security': {
        'handlers': ('error_console_handler',),
        'level': 'ERROR',
        'propagate': False,
    },
    'django.db.backends': {
        'handlers': ('info_console_handler',),
        'level': 'DEBUG',
        'propagate': False,
    },
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {'default': _DEFAULT_MESSAGE_FORMATTER, },
    'handlers': _LOG_HENDLERS,
    'loggers': _LOGGERS,
}
