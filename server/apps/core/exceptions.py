from typing import final

from server.exceptions import ServiceFailed


@final
class UnvalidFolderName(ServiceFailed):
    '''
    Raises when a course folder name validation error occurs.
    '''
    pass
