from typing import Protocol


class CourseRepository(Protocol):
    '''
    Interface of data access object for learning courses.
    '''

    def fetch_course_names(self) -> tuple[str, ...]:
        ...
