from typing import final

from django.db import Error as DatabaseError
from server.apps.request_folders.domain.entities import LearningCourse, RegionalOrganization
from server.apps.request_folders.domain.value_objects import CourseId, OrganizationId
from server.apps.request_folders.models import Course, VOSOrganization
from server.common.domain import EntityId
from server.common.infrastructure import make_safe
from ulid import ULID


@final
class LearningCourseDjangoRepository:
    '''
    Manages training course data in the database.
    '''
    __slots__ = ('__courses_data_manager')


    def __init__(self) -> None:
        self.__courses_data_manager = Course.objects


    @make_safe(DatabaseError)
    def fetch_all(self) -> tuple[LearningCourse, ...]:
        queryset = self.__courses_data_manager.values_list()
        return tuple(self.__build_entity(row) for row in queryset)


    @make_safe(DatabaseError)
    def exists(self) -> bool:
        return self.__courses_data_manager.exists()


    def __build_entity(self, src: tuple[ULID, str, str]) -> LearningCourse:
        identity = CourseId(EntityId(src[0]))
        return LearningCourse(identity, src[1], src[2])


@final
class RegionalOrganizationDjangoRepository:
    __slots__ = ('__data_manager')


    def __init__(self) -> None:
        self.__data_manager = VOSOrganization.objects


    @make_safe(DatabaseError)
    def fetch_all(self) -> tuple[RegionalOrganization, ...]:
        queryset = self.__data_manager.values_list()
        return tuple(self.__build_entity(row) for row in queryset)


    @make_safe(DatabaseError)
    def exists(self) -> bool:
        return self.__data_manager.exists()


    def __build_entity(self, src: tuple[ULID, str]) -> RegionalOrganization:
        identity = OrganizationId(EntityId(src[0]))
        return RegionalOrganization(identity, src[1])
