'''
Implementation of data access objects.
'''

from typing import Any, final, Iterable

from server.apps.learning_requests.models import Course


@final
class CourseDBRepo:
    '''
    Manages training course data in the database.
    '''

    def fetch_fields_lazy(self, *fild_names: str) -> Iterable[tuple[Any, ...]]:
        '''
        Returns an iterator that load all records about learning courses from the database.
        '''

        queryset = Course.objects.values_list(*fild_names)
        return queryset.iterator()


    def fetch_course_name_by_slug(self, slug: str) -> str | None:
        queryset = Course.objects.values_list('name', flat=True)
        try:
            course_name = queryset.get(slug=slug)
        except Course.DoesNotExist:
            return None
        else:
            return course_name


    def has_any_course(self) -> bool:
        return Course.objects.exists()
