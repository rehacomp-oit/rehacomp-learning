'''
Implementation of data access objects.
'''

from typing import final

from .models import Course


@final
class CourseDBRepo:
    '''
    Manages training course data in the database.
    '''

    def fetch_course_names(self) -> tuple[str, ...]:
        '''
        Returns all full names of training courses from database.
        '''

        queryset = Course.objects.values_list('course_name', flat=True)
        return tuple(queryset.all())
