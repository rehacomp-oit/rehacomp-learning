from typing import final

from django.db import Error as DatabaseError
from server.apps.request_folders.domain.entities import CourseFolder
from server.apps.request_folders.domain.value_objects import CourseFolderId
from server.apps.request_folders.models import Course
from server.common.domain import EntityId
from server.common.exceptions import MissingDataError
from server.common.infrastructure import make_safe
from ulid import ULID


@final
class CourseFolderDjangoRepository:
    '''
    Manages training course data in the database.
    '''

    __slots__ = ()


    @make_safe(DatabaseError)
    def fetch_all(self) -> tuple[CourseFolder, ...]:
        if not Course.objects.exists():
            raise MissingDataError
        else:
            queryset = Course.objects.values_list()
            return tuple(self.__to_entity(raw) for raw in queryset.iterator())


    def __to_entity(self, raw_data: tuple[ULID, str, str]) -> CourseFolder:
        return CourseFolder(
            CourseFolderId(EntityId(raw_data[0])),
            raw_data[1],
            raw_data[2]
        )
