from typing import final

from server.common.exceptions import BusinessLogicFailed

from .constants import COURSE_FULL_NAME_LENGTH


@final
class InvalidFolderName(BusinessLogicFailed):
    '''
    Exception type, connected with incorrect name of the learning course folder.
    '''

    def __init__(self, folder_name: str) -> None:
        self.folder_name = folder_name
        message = (
            'Folder name must not be an empty string and '
            f'must be at least {COURSE_FULL_NAME_LENGTH} characters long!'
        )
        super().__init__(message)
