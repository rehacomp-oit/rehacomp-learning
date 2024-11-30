'''
This module defines a set of protocols that establish
common interfaces for the entire project, promoting consistency
and type safety across various components.
'''

from typing import Any, Protocol


class HTTPRequestProtocol(Protocol):
    '''
    Outlines a protocol for HTTP request objects, defining a simple contract
    that Django request objects must adhere to, while abstracting away
    the implementation details of the framework.
    '''

    GET: dict[str, Any]
    POST: dict[str, Any]
    COOKIES: dict[str, str]
    method: str
    path: str
    headers: dict[str, str]
    body: str | bytes


class HTTPResponseProtocol(Protocol):
    '''
    Defines a protocol for HTTP response objects, establishing a clear contract
    that Django response objects must comply with, while abstracting from
    the framework's implementation details.
    '''

    status_code: int
    headers: dict[str, str]
    body: str | bytes
    content_type: str | None


class HttpController(Protocol):
    '''
    Defines a protocol for customized Django views, enabling greater flexibility
    in application design by adhering to clean architecture principles.
    '''

    def __call__(self, request: HTTPRequestProtocol, *args, **kwargs) -> HTTPResponseProtocol:
        ...
