from dataclasses import dataclass
from logging import Logger
from typing import final

from returns.result import Failure, Result, safe, Success
from server.common.exceptions import InfrastructureLayerError

from ..domain.dto import CourseFolder
from ..domain.entities import LearningCourse
from ..domain.protocols.repositories import LearningCourseRepository
from ..domain.results import GetCourseFoldersFailure


@final
@dataclass(frozen=True, slots=True)
class GetCourseFoldersService:
    repository: LearningCourseRepository
    logger: Logger


    def __call__(self) -> Result[tuple[CourseFolder, ...], GetCourseFoldersFailure]:
        return self._load_all_courses()\
            .alt(self._handle_infrastructure_error)\
            .bind_result(self._process_selected_data)


    @safe(exceptions=(InfrastructureLayerError,))
    def _load_all_courses(self) -> tuple[LearningCourse, ...] | None:
        if not self.repository.exists():
            return None

        return self.repository.fetch_all()


    def _handle_infrastructure_error(self, exception_object: Exception) -> GetCourseFoldersFailure:
        return GetCourseFoldersFailure.CRITICAL_FAILURE


    def _process_selected_data(
        self,
        courses: tuple[LearningCourse, ...] | None
    ) -> Result[tuple[CourseFolder, ...], GetCourseFoldersFailure]:
        if courses is None:
            return Failure(GetCourseFoldersFailure.MISSING_DATA)
        else:
            dto = tuple(CourseFolder(course.name, course.slug) for course in courses)
            return Success(dto)
