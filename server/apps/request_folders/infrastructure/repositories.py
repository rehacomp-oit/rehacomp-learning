from typing import final, TypeAlias

from server.apps.request_folders.domain.entities import CourseFolder
from server.apps.request_folders.domain.value_objects import CourseFolderId
from server.apps.request_folders.models import Course
from ulid import ULID


@final
class CourseFolderDjangoRepository:
    '''
    Manages training course data in the database.
    '''

    __RawData: TypeAlias = tuple[ULID, str, str]


    def fetch_all(self) -> tuple[CourseFolder, ...]:
        queryset = Course.objects.values_list()
        return tuple(self.__to_entity(raw) for raw in queryset.iterator())


    def fetch_by_slug(self, course_folder_slug: str) -> CourseFolder:
        queryset = Course.objects.values_list()
        return self.__to_entity(queryset.get(slug=course_folder_slug))


    def is_empty(self) -> bool:
        return not Course.objects.exists()


    def __to_entity(self, raw_data: __RawData) -> CourseFolder:
        return CourseFolder(
            CourseFolderId(raw_data[0]),
            raw_data[1],
            raw_data[2]
        )
