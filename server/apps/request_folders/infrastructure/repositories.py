from typing import final

from django.db import Error as DatabaseError
from server.apps.request_folders.domain.value_objects import CourseFolder, RequestFormOptions
from server.apps.request_folders.models import Course, VOSOrganization
from server.common.infrastructure import make_safe


@final
class CourseFolderDjangoRepository:
    '''
    Manages training course data in the database.
    '''
    __slots__ = ('__courses_data_manager')


    def __init__(self) -> None:
        self.__courses_data_manager = Course.objects


    @make_safe(DatabaseError)
    def fetch_all(self) -> tuple[CourseFolder, ...]:
        if not self.__courses_data_manager.exists():
            return ()
        else:
            queryset = self.__courses_data_manager.values_list('name', 'slug')
            return tuple(CourseFolder(*row) for row in queryset)


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
    def fetch(self) -> RequestFormOptions | None:
        '''
        Retrieves the value object with all organizations and courses from the database.

        Returns:
            the collected value object listing Courses and organizations.
        '''

        if not self.__courses_data_manager.exists() or not self.__organizations_data_manager.exists():
            return None

        field_names = ('id', 'name',)
        course_data_QS = self.__courses_data_manager.values_list(*field_names)
        organization_data_QS = self.__organizations_data_manager.values_list(*field_names)
        transform = lambda item: (str(item[0]), item[1])
        return RequestFormOptions(
            tuple(transform(row) for row in course_data_QS),
            tuple(transform(row) for row in organization_data_QS)
        )
