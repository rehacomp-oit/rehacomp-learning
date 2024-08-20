from dataclasses import dataclass
from typing import final

from returns.result import Failure, Success

from .domain.entities import CourseFolder
from .domain.exceptions import InvalidFolderMetadata
from .protocols.repositories import CourseRepository
from .protocols.results import CourseFoldersListServiceResult, FolderListFailure


@final
@dataclass(frozen=True, slots=True)
class CourseFoldersListService:
    '''
    Retrieves the full list of course folders.
    '''

    repository: CourseRepository


    def __call__(self) -> CourseFoldersListServiceResult:
        try:
            folders = tuple(
                CourseFolder.from_raw_data(record.id, record.course_name)
                for record in self.repository.fetch_all_lazy()
            )
        except InvalidFolderMetadata:
            return Failure(FolderListFailure.BROKEN_FOLDER_NAME)

        if not folders:
            return Failure(FolderListFailure.EMPTY_LIST)
        else:
            return Success(folders)
