'''
Common exception types for this project.
'''

from typing import final


class ApplicationError(Exception):
    '''
    Base exception for this application.
    '''
    pass


class BusinessLogicFailed(ApplicationError):
    '''
    Unsuccessful execution of a business operation.
    '''
    pass


@final
class InvalidIdentifier(BusinessLogicFailed):
    '''
    Error occurred when the integer identifier value was incorrect.
    '''

    def __init__(self, invalid_id: int) -> None:
        self.invalid_id = invalid_id
        self.message = 'Value must be a positive integer'
        super().__init__(self.message)


    def __str__(self) -> str:
        return f'{self.invalid_id} -> {self.message}'
