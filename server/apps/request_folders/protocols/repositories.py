from typing import Protocol

from server.apps.request_folders.domain.entities import CourseFolder
from server.apps.request_folders.domain.value_objects import RequestFormOptions


class CourseFolderRepository(Protocol):
    '''
    Interface of data access object for learning courses.
    '''

    def fetch_all(self) -> tuple[CourseFolder, ...]:
        ...


class RequestFormOptionsRepository(Protocol):
    '''
    Interface of data access object for VOS organizations.
    '''

    def fetch(self) -> RequestFormOptions:
        ...
