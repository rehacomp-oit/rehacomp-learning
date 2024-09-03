from enum import StrEnum
from typing import final, TypeAlias

from returns.result import Result
from server.apps.learning_requests.domain.constants import COURSE_FULL_NAME_LENGTH
from server.apps.learning_requests.domain.value_objects import CourseFolderName


@final
class FolderListFailure(StrEnum):
    EMPTY_LIST = 'empty folder list'
    BROKEN_FOLDER_NAME = (
        f'The course name should not be empty and should have no more than {COURSE_FULL_NAME_LENGTH} characters'
    )


CourseFoldersListServiceResult: TypeAlias = Result[tuple[CourseFolderName, ...], FolderListFailure]
