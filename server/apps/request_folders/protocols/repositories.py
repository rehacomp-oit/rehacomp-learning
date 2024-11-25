from typing import Protocol

from server.apps.request_folders.domain.entities import CourseFolder, VosOrganization


class CourseFolderRepository(Protocol):
    '''
    Interface of data access object for learning courses.
    '''

    def fetch_all(self) -> tuple[CourseFolder, ...]:
        ...


class VOSOrganizationRepository(Protocol):
    '''
    Interface of data access object for VOS organizations.
    '''


    def fetch_all(self) -> tuple[VosOrganization, ...]:
        ...
