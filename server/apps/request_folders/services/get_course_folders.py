from logging import getLogger
from typing import final

from returns.result import Failure, Result, Success
from server.common.exceptions import EmptyRepositoryError, InfrastructureLayerError
from server.common.helpers import define_service

from ..domain.dto import CourseFolder
from ..domain.entities import LearningCourse
from ..domain.protocols.repositories import LearningCourseRepository
from ..domain.results import GetCourseFoldersFailure


_logger = getLogger(__name__)


@final
@define_service
class GetCourseFoldersService:
    repository: LearningCourseRepository


    def __call__(self) -> Result[tuple[CourseFolder, ...], GetCourseFoldersFailure]:
        return self._load_all_courses().bind(self._make_output)


    def _load_all_courses(self) -> Result[tuple[LearningCourse, ...], GetCourseFoldersFailure]:
        try:
            courses = self.repository.fetch_all()
        except EmptyRepositoryError:
            _logger.info('Information about learning courses is missing')
            return Failure(GetCourseFoldersFailure.MISSING_DATA)
        except InfrastructureLayerError as exc:
            _logger.exception(exc)
            return Failure(GetCourseFoldersFailure.CRITICAL_FAILURE)
        else:
            return Success(courses)


    def _make_output(
        self,
        courses: tuple[LearningCourse, ...]
    ) -> Success[tuple[CourseFolder, ...]]:
        dto = tuple(CourseFolder(course.name, course.slug) for course in courses)
        return Success(dto)
