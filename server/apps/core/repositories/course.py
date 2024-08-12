from typing import final

from server.apps.core.models import Course


@final
class CourseDBRepository:
    '''
    Data access object to information about courses from the database.
    '''

    def load_course_full_names(self) -> tuple[str, ...]:
        queryset = Course.objects.values_list('course_name', flat=True)
        return tuple(queryset.all())
