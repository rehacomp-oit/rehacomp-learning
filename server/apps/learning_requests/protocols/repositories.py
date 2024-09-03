from typing import Any, Iterable, Protocol


class CourseRepository(Protocol):
    '''
    Interface of data access object for learning courses.
    '''

    def fetch_fields_lazy(self, *fild_names: str) -> Iterable[tuple[Any]]:
        ...


    def has_any_course(self) -> bool:
        ...
