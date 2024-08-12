from enum import StrEnum
from typing import final

from .constants import COURSE_FULL_NAME_LENGTH


@final
class FolderListFailure(StrEnum):
    EMPTY_LIST = 'empty'
    BROKEN_FOLDER_NAME = (
        f'The course name should not be empty and should have no more than {COURSE_FULL_NAME_LENGTH} characters'
    )
