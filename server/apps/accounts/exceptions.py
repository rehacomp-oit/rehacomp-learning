from typing import final


@final
class RepositoryError(Exception):
    '''
    Raised when repository operation cannot be completed due to infrastructure failure.
    '''
    __slots__ = ()


@final
class ServiceError(Exception):
    '''
    Raised when infrastructure service operation cannot be completed due to critical failure.
    '''
    __slots__ = ()
