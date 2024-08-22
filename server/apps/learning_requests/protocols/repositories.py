from typing import Iterable, Protocol

from server.apps.learning_requests.models import Course


class CourseRepository(Protocol):
    '''
    Interface of data access object for learning courses.
    '''

    def fetch_all_lazy(self) -> Iterable[Course]:
        ...


    def has_any_course(self) -> bool:
        ...
