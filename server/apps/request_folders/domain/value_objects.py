from dataclasses import dataclass
from typing import final, NewType
from uuid import UUID

from .constants import COURSE_FULL_NAME_LENGTH
from .exceptions import InvalidFolderName


CourseFolderId = NewType('CourseFolderId', UUID)


@final
@dataclass(frozen=True, slots=True)
class CourseFolderName:
    '''
    Value object representing the valid name of the learning course folder.
    '''

    name: str
    slug: str


    def __post_init__(self) -> None:
        if not self.name or len(self.name) > COURSE_FULL_NAME_LENGTH:
            raise InvalidFolderName(self.name)
