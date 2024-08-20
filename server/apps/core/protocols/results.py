from __future__ import annotations

from enum import StrEnum
from typing import final, TypeAlias

from returns.result import Result
from server.apps.core.domain.constants import COURSE_FULL_NAME_LENGTH
from server.apps.core.domain.entities import CourseFolder


@final
class FolderListFailure(StrEnum):
    EMPTY_LIST = 'empty folder list'
    BROKEN_FOLDER_NAME = (
        f'The course name should not be empty and should have no more than {COURSE_FULL_NAME_LENGTH} characters'
    )


CourseFoldersListServiceResult: TypeAlias = Result[tuple[CourseFolder, ...], FolderListFailure]
