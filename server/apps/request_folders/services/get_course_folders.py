from dataclasses import dataclass
from logging import Logger
from typing import final

from returns.io import IOResult
from returns.result import Failure, Result, Success
from server.apps.request_folders.domain.results import GetCourseFoldersFailure
from server.apps.request_folders.domain.value_objects import CourseFolder
from server.apps.request_folders.protocols.repositories import CourseFolderRepository


@final
@dataclass(frozen=True, slots=True)
class GetCourseFoldersService:
    logger: Logger
    repository: CourseFolderRepository


    def __call__(self) -> IOResult[tuple[CourseFolder, ...], GetCourseFoldersFailure]:
        return self.repository.fetch_all()\
            .alt(self._handle_infrastructure_error)\
            .bind_result(self._process_selected_data)


    def _handle_infrastructure_error(self, exception_object: Exception) -> GetCourseFoldersFailure:
        return GetCourseFoldersFailure.CRITICAL_FAILURE


    def _process_selected_data(
        self,
        data: tuple[CourseFolder, ...]
    ) -> Result[tuple[CourseFolder, ...], GetCourseFoldersFailure]:
        if not data:
            return Failure(GetCourseFoldersFailure.MISSING_DATA)
        else:
            return Success(data)
