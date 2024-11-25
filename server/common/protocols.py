from typing import Any, Protocol

from .django_tools import HtmxHttpRequest


class HttpController(Protocol):
    '''
    docs
    '''

    def __call__(self, request: HtmxHttpRequest, *args, **kwargs) -> Any:
        ...
