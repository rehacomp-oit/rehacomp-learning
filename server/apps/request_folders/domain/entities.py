from dataclasses import dataclass
from typing import final

from server.common.types import BaseEntity

from .value_objects import CourseFolderId


@final
@dataclass(slots=True)
class CourseFolder(BaseEntity):
    id: CourseFolderId  # noqa: VNE003
    name: str
    slug: str


    @property
    def course_abbreviation(self) -> str:
        '''
        Returns the generated abbreviation of the course name.
        '''

        words = self.name.split(' ')
        if len(words) == 1:
            return self.name[:3].upper()
        else:
            chars = [word[0] for word in words]
            return ''.join(chars).upper()
