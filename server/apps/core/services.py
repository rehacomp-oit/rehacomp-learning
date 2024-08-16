from dataclasses import dataclass
from typing import final

from returns.result import Failure, Success

from .business_error_types import FolderListFailure
from .protocols.repositories import CourseRepository
from .protocols.results import CourseFoldersListServiceResult
from .value_objects import CourseFolderName


@final
@dataclass(frozen=True, slots=True)
class CourseFoldersListService:
    '''
    Retrieves the full list of course folders.
    '''

    repository: CourseRepository


    def __call__(self) -> CourseFoldersListServiceResult:
        raw_data = self.repository.fetch_course_names()
        if not raw_data:
            return Failure(FolderListFailure.EMPTY_LIST)

        try:
            folder_list = tuple(CourseFolderName(item) for item in raw_data)
        except ValueError:
            return Failure(FolderListFailure.BROKEN_FOLDER_NAME)
        else:
            return Success(folder_list)
