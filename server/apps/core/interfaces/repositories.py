from typing import Protocol


class CourseRepository(Protocol):
    '''
    Interface for manipulating course data.
    '''

    def load_course_full_names(self) -> tuple[str, ...]:
        ...
