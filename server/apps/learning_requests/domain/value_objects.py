from typing import final, NewType, Self

from server.common.types import IntegerId

from .constants import COURSE_FULL_NAME_LENGTH


CourseFolderId = NewType('CourseFolderId', IntegerId)


@final
class CourseFolderName(str):
    '''
    Value object representing the valid name of the learning course folder.
    '''

    def __new__(cls, value: str) -> Self:
        if not value or len(value) > COURSE_FULL_NAME_LENGTH:
            raise ValueError('Invalid string value.')
        else:
            return super().__new__(cls, value)
