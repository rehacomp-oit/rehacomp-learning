from dataclasses import dataclass
from typing import final, NewType
from uuid import UUID

from server.common.types import BaseEntity


CourseFolderId = NewType('CourseFolderId', UUID)


@final
@dataclass(slots=True)
class CourseFolder(BaseEntity):
    id: CourseFolderId  # noqa: VNE003
    name: str
    slug: str


    @property
    def course_abbreviation(self) -> str:
        words = self.name.split(' ')
        if len(words) == 1:
            return self.name[:3].upper()
        else:
            chars = [word[0] for word in words]
            return ''.join(chars).upper()
