from logging import getLogger, Logger
from re import compile
from typing import Final

from pytest import fixture, LogCaptureFixture

_LOGGING_FORMAT_RE: Final = compile(
    r'timestamp=\'.+\' level=\'error\' event=\'Test message\' logger=\'django\'',
)


@fixture(name='logger')
def logger_fixture() -> Logger:
    '''Returns the current logger instance.'''
    return getLogger('django')


@fixture(autouse=True)
def _redact_caplog_handlers(
    caplog: LogCaptureFixture,
    logger: Logger
) -> None:
    '''Pytest inserts custom formatter, we need to reset it back.'''
    caplog.handler.setFormatter(logger.handlers[0].formatter)


def test_logging_format(
    caplog: LogCaptureFixture,
    logger: Logger
) -> None:
    '''This test ensures logging is done correctly.'''
    message = 'Test message'
    logger.error(message)
    assert _LOGGING_FORMAT_RE.match(caplog.text)
