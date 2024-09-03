from dataclasses import dataclass
from typing import final

from returns.result import Failure, Success
from server.apps.learning_requests.domain.exceptions import InvalidFolderName
from server.apps.learning_requests.domain.value_objects import CourseFolderName
from server.apps.learning_requests.protocols.repositories import CourseRepository
from server.apps.learning_requests.protocols.results import CourseFoldersListServiceResult, FolderListFailure


@final
@dataclass(frozen=True, slots=True)
class CourseFoldersListService:
    '''
    Retrieves the full list of course folders.
    '''

    repository: CourseRepository


    def __call__(self) -> CourseFoldersListServiceResult:
        if not self.repository.has_any_course():
            return Failure(FolderListFailure.EMPTY_LIST)

        try:
            folders = tuple(CourseFolderName(*row) for row in self.repository.fetch_fields_lazy('name', 'slug'))
        except InvalidFolderName:
            return Failure(FolderListFailure.BROKEN_FOLDER_NAME)
        else:
            return Success(folders)
