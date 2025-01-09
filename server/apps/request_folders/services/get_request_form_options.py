from __future__ import annotations

from dataclasses import dataclass
from logging import Logger
from typing import final

from returns.pipeline import flow
from returns.pointfree import bind
from returns.result import Failure, Result, Success
from server.common.exceptions import EmptyRepositoryError, InfrastructureLayerError

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
            self._load_all_courses,
            bind(self._load_all_organizations),
            bind(self._load_translations),
            bind(self._build_output)
        )


    def _load_all_courses(self, context: _InternalContext) -> Result[_InternalContext, GetRequestFormOptionFailure]:
        try:
            context.courses = self.course_repository.fetch_all()
        except EmptyRepositoryError:
            return Failure(GetRequestFormOptionFailure.MISSING_DATA)
        except InfrastructureLayerError:
            return Failure(GetRequestFormOptionFailure.CRITICAL_FAILURE)
        else:
            return Success(context)


    def _load_all_organizations(
        self,
        context: _InternalContext
    ) -> Result[_InternalContext, GetRequestFormOptionFailure]:
        try:
            context.organizations = self.organization_repository.fetch_all()
        except EmptyRepositoryError:
            return Failure(GetRequestFormOptionFailure.MISSING_DATA)
        except InfrastructureLayerError:
            return Failure(GetRequestFormOptionFailure.CRITICAL_FAILURE)
        else:
            return Success(context)


    def _load_translations(self, context: _InternalContext) -> Success[_InternalContext]:
        context.disability_groups = self.disability_group_translator.get_all_translations()
        context.training_levels = self.training_level_translator.get_all_translations()
        return Success(context)


    def _build_output(self, context: _InternalContext) -> Success[RequestFormOptions]:
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
