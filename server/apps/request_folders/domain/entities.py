from datetime import datetime, timezone
from typing import final

from server.common.domain import define_entity, Entity, entity_field

from .enum_types import DisabilityGroup, LearningRequestStatus, TrainingLevel
from .value_objects import CourseId, LearningRequestId, OrganizationCode, OrganizationId, PersonId


@final
@define_entity
class LearningCourse(Entity):
    id: CourseId  # noqa: VNE003
    name: str
    slug: str


    def get_course_short_name(self) -> str:
        '''
        Returns the generated abbreviation of the course name.
        '''

        words = self.name.split(' ')
        if len(words) == 1:
            return self.name[:3].upper()
        else:
            chars = (word[0] for word in words)
            return ''.join(chars).upper()


@final
@define_entity
class RegionalOrganization(Entity):
    id: OrganizationId  # noqa: VNE003
    name: str
    code: OrganizationCode


@final
@define_entity
class Person(Entity):
    id: PersonId  # noqa: VNE003
    first_name: str
    patronymic: str
    last_name: str
    birth_year: int
    disability_group: DisabilityGroup
    vos_organization: RegionalOrganization
    training_level: TrainingLevel
    education_info: str = ''
    job_info: str = ''
    is_known_braille: bool = False
    has_device: bool = True
    personal_phone: str = ''
    email: str = ''


@final
@define_entity
class LearningRequestCart(Entity):
    id: LearningRequestId  # noqa: VNE003
    course: LearningCourse
    candidate: Person
    created_at: datetime = entity_field(default=datetime.now(tz=timezone.utc))
    updated_at: datetime | None = entity_field(default=None)
    note: str = entity_field(default='')
    status: LearningRequestStatus = entity_field(default=LearningRequestStatus.REQUEST)
    relevance: bool = entity_field(default=True)


    def mark_as_irrelevant(self, reason: str | None=None) -> None:
        self.relevance = False
        if reason is not None:
            self.note = reason
        else:
            self.note = 'В архиве'


    def deny(self) -> None:
        self.status = LearningRequestStatus.REJECTION
