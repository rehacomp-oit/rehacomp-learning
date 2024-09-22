from dataclasses import dataclass
from typing import final, NewType

from server.common.types import BaseEntity, IntegerId


CourseFolderId = NewType('CourseFolderId', IntegerId)


@final
@dataclass(slots=True)
class CourseFolder(BaseEntity):
    id: CourseFolderId  # noqa: VNE003
    name: str
    slug: str
