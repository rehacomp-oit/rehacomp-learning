'''
Implementation of a common infrastructure layer.
'''

from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

from returns.io import IOFailure, IOResultE, IOSuccess
from ulid import new as generate_ulid

from .domain import EntityId


# Annotation helpers for decorators definition:
F_Spec = ParamSpec('F_Spec')
F_Return = TypeVar('F_Return')


def get_ulid_for_pk() -> EntityId:
    '''
    Returns the generated ULID for the domain entity
    '''

    return EntityId(generate_ulid())


def make_safe(
    expected_exception: type[Exception] | None=None
) -> Callable[[Callable[F_Spec, F_Return]], Callable[F_Spec, IOResultE[F_Return]]]:
    '''
    Wraps functions or methods of the infrastructure layer, ensuring error handling.

    If a specified exception is raised, the decorator will raise an <InfrastructureLayerError> exception.
    If no exception is passed to the decorator, the base Exception class will be caught.

    :param expected_exception: The specific exception type to catch during the function's execution.
    If not provided, it will default to capturing all exceptions derived from the base Exception.

    :raises InfrastructureLayerError: if specified or general exception occurs.
    '''

    def _decorate(operation: Callable[F_Spec, F_Return]) -> Callable[F_Spec, IOResultE[F_Return]]:
        @wraps(operation)
        def _wrapper(*args: F_Spec.args, **kwargs: F_Spec.kwargs) -> IOResultE[F_Return]:
            ExceptionClass = expected_exception or Exception
            try:
                return IOSuccess(operation(*args, **kwargs))
            except ExceptionClass as catched:
                return IOFailure(catched)

        return _wrapper
    return _decorate
