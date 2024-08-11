'''
Base exception types for the project.
'''


class AppError(Exception):
    '''
    Base exception for this application.
    '''
    pass


class ServiceFailed(AppError):
    '''
    Unsuccessful execution of a business scenario.
    '''
    pass
