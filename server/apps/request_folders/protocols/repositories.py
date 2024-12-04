from typing import Protocol

from returns.io import IOResultE
from server.apps.request_folders.domain.value_objects import CourseFolder, RequestFormOptions


class CourseFolderRepository(Protocol):
    '''
    Interface of data access object for learning courses.
    '''

    def fetch_all(self) -> IOResultE[tuple[CourseFolder, ...]]:
        ...


class RequestFormOptionsRepository(Protocol):
    '''
    Interface of data access object for VOS organizations.
    '''

    def fetch(self) -> IOResultE[RequestFormOptions | None]:
        ...
