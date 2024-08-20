'''
Base exception types for this project.
'''


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
