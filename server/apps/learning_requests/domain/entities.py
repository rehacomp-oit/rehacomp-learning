from dataclasses import dataclass
from typing import final, Self

from server.common.types import IntegerId

from .exceptions import InvalidFolderMetadata
from .value_objects import CourseFolderId, CourseFolderName


@final
@dataclass(slots=True)
class CourseFolder:
    id: CourseFolderId  # noqa: VNE003
    name: CourseFolderName


    @classmethod
    def from_raw_data(cls, course_id: int, course_name: str) -> Self:
        try:
            folder_id = CourseFolderId(IntegerId(course_id))
            folder_name = CourseFolderName(course_name)
        except ValueError as error:
            raise InvalidFolderMetadata from error
        else:
            return cls(folder_id, folder_name)
