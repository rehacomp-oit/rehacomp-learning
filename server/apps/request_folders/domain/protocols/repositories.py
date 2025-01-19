from typing import Protocol

from ..entities import LearningCourse, RegionalOrganization


class LearningCourseRepository(Protocol):
    '''
    Interface of data access object for learning courses.
    '''

    def fetch_all(self) -> tuple[LearningCourse, ...]:
        ...


class RegionalOrganizationRepository(Protocol):
    '''
    Interface of data access object for VOS organizations.
    '''

    def fetch_all(self) -> tuple[RegionalOrganization, ...]:
        ...
