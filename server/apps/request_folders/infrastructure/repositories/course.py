from typing import final, TypedDict

from django.db import Error as DatabaseError
from server.apps.request_folders.domain.entities import LearningCourse
from server.apps.request_folders.domain.value_objects import CourseId
from server.apps.request_folders.models import Course
from server.common.domain import EntityId
from server.common.infrastructure import make_safe
from ulid import ULID


@final
class _DBInternal(TypedDict):
    id: ULID  # noqa: VNE003
    name: str
    slug: str


@final
class LearningCourseDjangoRepository:
    '''
    Manages training course data in the database.
    '''
    __slots__ = ('__manager')


    def __init__(self) -> None:
        self.__manager = Course.objects


    @make_safe(DatabaseError)
    def fetch_all(self) -> tuple[LearningCourse, ...]:
        queryset = self.__manager.order_by('name').values()
        return tuple(self.__build_entity(row) for row in queryset)


    @make_safe(DatabaseError)
    def exists(self) -> bool:
        return self.__manager.exists()


    def __build_entity(self, src: _DBInternal) -> LearningCourse:
        course_id = CourseId(EntityId(src['id']))
        return LearningCourse(course_id, src['name'], src['slug'])
