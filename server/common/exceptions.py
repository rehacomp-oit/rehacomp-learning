'''
Common exception types for this project.
'''

from typing import final


class BaseError(Exception):
    '''
    Base exception for this application.

    this exception should not be used directly.
    '''
    pass


class InfrastructureLayerError(BaseError):
    '''
    Critical error in the application infrastructure layer.
    '''

    def __init__(self, optional_message: str | None=None) -> None:
        message = optional_message or 'Critical error in the application infrastructure!'
        super().__init__(message)


@final
class ControllerError(InfrastructureLayerError):
    '''
    Critical http controller error caused by problems with the application infrastructure.
    '''

    def __init__(self, reason: str) -> None:
        message = f'Internal application error! Reason: "{reason}".'
        self.reason = reason
        super().__init__(message)


@final
class EmptyRepositoryError(InfrastructureLayerError):
    '''
    The requested data was not found.
    '''
    pass
