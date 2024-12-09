from dataclasses import dataclass
from logging import Logger
from typing import final, TypeAlias

from returns.result import Failure, Result, safe, Success
from server.common.exceptions import InfrastructureLayerError

from ..domain.dto import RequestFormOptions
from ..domain.entities import LearningCourse, RegionalOrganization
from ..domain.protocols.repositories import LearningCourseRepository, RegionalOrganizationRepository
from ..domain.results import GetRequestFormOptionFailure


_Raw_data: TypeAlias = tuple[tuple[LearningCourse, ...], tuple[RegionalOrganization, ...]]


@final
@dataclass(frozen=True, slots=True)
class GetRequestFormOptionsService:
    course_repository: LearningCourseRepository
    organization_repository: RegionalOrganizationRepository
    logger: Logger


    def __call__(self) -> Result[RequestFormOptions, GetRequestFormOptionFailure]:
        return self._load_courses_with_organizations()\
            .alt(self._handle_infrastructure_error)\
            .bind_result(self._build_output)


    @safe(exceptions=(InfrastructureLayerError,))
    def _load_courses_with_organizations(self) -> _Raw_data | None:
        if not self.course_repository.exists() or not self.organization_repository.exists():
            return None

        return (self.course_repository.fetch_all(), self.organization_repository.fetch_all(),)


    def _handle_infrastructure_error(self, exception_object: Exception) -> GetRequestFormOptionFailure:
        return GetRequestFormOptionFailure.CRITICAL_FAILURE


    def _build_output(self, data: _Raw_data | None) -> Result[RequestFormOptions, GetRequestFormOptionFailure]:
        if data is None:
            return Failure(GetRequestFormOptionFailure.MISSING_DATA)

        courses, organizations = data
        options = RequestFormOptions(
            tuple((str(course.id), course.name) for course in courses),
            tuple((str(organization.id), organization.name) for organization in organizations)
        )
        return Success(options)
