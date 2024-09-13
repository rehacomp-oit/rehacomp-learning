from dataclasses import dataclass
from typing import final

from returns.result import Failure, Success
from server.apps.learning_requests.domain.exceptions import InvalidFolderName
from server.apps.learning_requests.domain.value_objects import CourseFolderName
from server.apps.learning_requests.protocols.repositories import CourseRepository
from server.apps.learning_requests.protocols.services import CourseFoldersListResult
from server.common.types import FailureReason


@final
@dataclass(frozen=True, slots=True)
class CourseFoldersListService:
    '''
    Retrieves the full list of course folders.
    '''

    repository: CourseRepository


    def __call__(self) -> CourseFoldersListResult:
        if not self.repository.has_any_course():
            return Success(())

        try:
            folders = tuple(CourseFolderName(*row) for row in self.repository.fetch_fields_lazy('name', 'slug'))
        except InvalidFolderName:
            return Failure(FailureReason('Broken folder name!'))
        else:
            return Success(folders)
