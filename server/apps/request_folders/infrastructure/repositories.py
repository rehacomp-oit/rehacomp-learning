'''
Implementation of data access objects.
'''

from typing import final, TypeAlias

from server.apps.request_folders.domain.entities import CourseFolder
from server.apps.request_folders.domain.value_objects import CourseFolderId
from server.apps.request_folders.models import Course
from server.core.infrastructure import BaseRepository
from ulid import ULID


@final
class CourseRepository(BaseRepository):
    '''
    Manages training course data in the database.
    '''

    _model = Course
    __RawData: TypeAlias = tuple[ULID, str, str]


    def _to_entity(self, raw_data: __RawData) -> CourseFolder:
        return CourseFolder(
            CourseFolderId(raw_data[0].uuid),
            raw_data[1],
            raw_data[2]
        )
