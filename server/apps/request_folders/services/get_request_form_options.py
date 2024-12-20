from __future__ import annotations

from dataclasses import dataclass
from logging import Logger
from typing import final

from returns.pipeline import flow
from returns.pointfree import alt, bind
from returns.result import Failure, Result, safe, Success
from server.common.exceptions import InfrastructureLayerError

from ..domain.dto import RequestFormOptions
from ..domain.entities import LearningCourse, RegionalOrganization
from ..domain.protocols.repositories import LearningCourseRepository, RegionalOrganizationRepository
from ..domain.protocols.translators import DisabilityGroupTranslator, TrainingLevelTranslator
from ..domain.results import GetRequestFormOptionFailure


@final
@dataclass(frozen=True, slots=True)
class GetRequestFormOptionsService:
    course_repository: LearningCourseRepository
    organization_repository: RegionalOrganizationRepository
    disability_group_translator: DisabilityGroupTranslator
    training_level_translator: TrainingLevelTranslator
    logger: Logger


    def __call__(self) -> Result[RequestFormOptions, GetRequestFormOptionFailure]:
        return flow(
            _InternalContext(),
            self._load_courses_with_organizations,
            alt(self._handle_infrastructure_error),
            bind(self._load_translations),
            bind(self._build_output)
        )


    @safe(exceptions=(InfrastructureLayerError,))
    def _load_courses_with_organizations(self, context: _InternalContext) -> _InternalContext:
        if not self.course_repository.exists() or not self.organization_repository.exists():
            context.courses, context.organizations = (), ()
            return context

        context.courses = self.course_repository.fetch_all()
        context.organizations = self.organization_repository.fetch_all()
        return context


    def _handle_infrastructure_error(self, exception_object: Exception) -> GetRequestFormOptionFailure:
        return GetRequestFormOptionFailure.CRITICAL_FAILURE


    def _load_translations(self, context: _InternalContext) -> Success[_InternalContext]:
        context.disability_groups = self.disability_group_translator.get_all_translations()
        context.training_levels = self.training_level_translator.get_all_translations()
        return Success(context)


    def _build_output(self, context: _InternalContext) -> Result[RequestFormOptions, GetRequestFormOptionFailure]:
        if not context.courses and not context.organizations:
            return Failure(GetRequestFormOptionFailure.MISSING_DATA)

        course_choices = tuple(
            (course.slug, course.name) for course in context.courses
        )

        organization_choices = tuple(
            (str(organization.code), organization.name) for organization in context.organizations
        )

        output = RequestFormOptions(
            course_choices,
            organization_choices,
            context.disability_groups,
            context.training_levels
        )
        return Success(output)


class _InternalContext:
    __slots__ = ('courses', 'organizations', 'disability_groups', 'training_levels',)

    courses: tuple[LearningCourse, ...]
    organizations: tuple[RegionalOrganization, ...]
    disability_groups: tuple[tuple[int, str], ...]
    training_levels: tuple[tuple[int, str], ...]
