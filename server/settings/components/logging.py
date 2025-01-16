'''
Settings for the logging mechanism of the project
'''

from __future__ import annotations

from collections.abc import Callable
from typing import final, TYPE_CHECKING

import structlog

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


_json_formatter = {
    '()': structlog.stdlib.ProcessorFormatter,
    'processor': structlog.processors.JSONRenderer(),
}

_console = {
    '()': structlog.stdlib.ProcessorFormatter,
    'processor': structlog.processors.KeyValueRenderer(key_order=['timestamp', 'level', 'event', 'logger']),
    'foreign_pre_chain': [
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.TimeStamper(fmt='iso'),
    ],
}


_hendlers = {
    'console': {'class': 'logging.StreamHandler', 'formatter': 'console', },
    'json_console': {'class': 'logging.StreamHandler', 'formatter': 'json_formatter', },
}


_LOGGERS = {
    'server': {
        'handlers': ('console',),
        'propagate': False,
        'level': 'INFO',
    },
    'django': {
        'handlers': ('console',),
        'propagate': True,
        'level': 'INFO',
    },
    'security': {
        'handlers': ('console',),
        'level': 'ERROR',
        'propagate': False,
    },
    'django.db.backends': {
        'handlers': ('console',),
        'level': 'DEBUG',
        'propagate': False,
    },
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {'json_formatter': _json_formatter, 'console': _console, },
    'handlers': _hendlers,
    'loggers': _LOGGERS,
}


@final
class LoggingContextVarsMiddleware:
    '''Used to reset ContextVars in structlog on each request.'''

    def __init__(
        self,
        get_response: Callable[[HttpRequest], HttpResponse],
    ) -> None:
        '''Django\'s API-compatible constructor.'''
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        '''
        Handle requests.

        Add your logging metadata here.
        Example: https://github.com/jrobichaud/django-structlog
        '''
        response = self.get_response(request)
        structlog.contextvars.clear_contextvars()
        return response


if not structlog.is_configured():
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.stdlib.filter_by_level,
            structlog.processors.TimeStamper(fmt='iso'),
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.ExceptionPrettyPrinter(),
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
