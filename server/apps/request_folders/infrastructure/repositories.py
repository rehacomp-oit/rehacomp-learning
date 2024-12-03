from typing import final

from django.db import Error as DatabaseError
from server.apps.request_folders.domain.entities import CourseFolder
from server.apps.request_folders.domain.value_objects import CourseFolderId, RequestFormOptions
from server.apps.request_folders.models import Course, VOSOrganization
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


@final
class RequestFormOptionsDjangoRepository:
    '''
    Implementation of the django repository for data management of the learning request registration form.

    This class handles the retrieval and management of value objects that represent
    from the database information about learning courses and VOS organizations
    for registration learning request.
    '''
    __slots__ = ('__courses_data_manager', '__organizations_data_manager')


    def __init__(self) -> None:
        self.__courses_data_manager = Course.objects
        self.__organizations_data_manager = VOSOrganization.objects


    @make_safe(DatabaseError)
    def fetch(self) -> RequestFormOptions:
        '''
        Retrieves the value object with all organizations and courses from the database.

        Raises:
            MissingDataError: If there is no course or organization data present in the database.

        Returns:
            the collected value object listing Courses and organizations.
        '''

        if not self.__courses_data_manager.exists() or not self.__organizations_data_manager.exists():
            raise MissingDataError

        field_names = ('id', 'name',)
        course_data_QS = self.__courses_data_manager.values_list(*field_names)
        organization_data_QS = self.__organizations_data_manager.values_list(*field_names)
        transform = lambda item: (str(item[0]), item[1])
        return RequestFormOptions(
            tuple(transform(row) for row in course_data_QS),
            tuple(transform(row) for row in organization_data_QS)
        )
