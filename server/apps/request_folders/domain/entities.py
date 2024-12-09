from dataclasses import dataclass
from typing import final

from server.common.domain import Entity

from .value_objects import CourseId, OrganizationId


@final
@dataclass(slots=True)
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
@dataclass(slots=True)
class RegionalOrganization(Entity):
    id: OrganizationId  # noqa: VNE003
    name: str
