from typing import final, TypedDict

from django.core.cache import cache
from server.apps.request_folders.domain.entities import LearningCourse
from server.apps.request_folders.domain.value_objects import CourseId
from server.apps.request_folders.models import Course
from server.common.domain import EntityId
from server.common.exceptions import EmptyRepositoryError
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

    __slots__ = (
        '__cache_timeout',
        '__courses_cache',
    )


    def __init__(self) -> None:
        # 10 minutes
        self.__cache_timeout = 600
        self.__courses_cache = 'courses'


    @make_safe
    def fetch_all(self) -> tuple[LearningCourse, ...]:
        courses = cache.get(self.__courses_cache)
        if courses is not None:
            return courses

        queryset = Course.objects.order_by('name').values()
        courses = tuple(self.__build_entity(row) for row in queryset)
        if not courses:
            raise EmptyRepositoryError('msg')

        cache.set(self.__courses_cache, courses, self.__cache_timeout)
        return courses


    def __build_entity(self, src: _DBInternal) -> LearningCourse:
        course_id = CourseId(EntityId(src['id']))
        return LearningCourse(course_id, src['name'], src['slug'])
