from typing import final

from server.common.domain import define_entity, Entity

from .value_objects import CourseId, OrganizationCode, OrganizationId


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
