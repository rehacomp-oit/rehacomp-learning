from logging import getLogger
from typing import final

from returns.result import Failure, Result, Success
from server.common.exceptions import EmptyRepositoryError, InfrastructureLayerError
from server.common.helpers import define_service

from ..domain.dto import CourseDTO
from ..domain.entities import LearningCourse
from ..domain.protocols.repositories import LearningCourseRepository
from ..domain.results import GetCourseFoldersFailure


_logger = getLogger(__name__)


@final
@define_service
class GetCourseListService:
    repository: LearningCourseRepository


    def __call__(self) -> Result[tuple[CourseDTO, ...], GetCourseFoldersFailure]:
        return self._load_data().bind(self._make_output)


    def _load_data(self) -> Result[tuple[LearningCourse, ...], GetCourseFoldersFailure]:
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
    ) -> Success[tuple[CourseDTO, ...]]:
        dto = tuple(CourseDTO(course.name, course.slug) for course in courses)
        return Success(dto)
