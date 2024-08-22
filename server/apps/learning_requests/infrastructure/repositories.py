'''
Implementation of data access objects.
'''

from typing import final, Iterable

from server.apps.learning_requests.models import Course


@final
class CourseDBRepo:
    '''
    Manages training course data in the database.
    '''

    def fetch_all_lazy(self) -> Iterable[Course]:
        '''
        Returns an iterator that load all records about learning courses from the database.
        '''

        queryset = Course.objects.all()
        return queryset.iterator()


    def has_any_course(self) -> bool:
        return Course.objects.exists()
