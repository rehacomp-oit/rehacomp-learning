from dataclasses import dataclass
from typing import final


@final
@dataclass(frozen=True, slots=True)
class CourseFolder:
    name: str
    reference: str


@final
@dataclass(frozen=True, slots=True)
class RequestFormOptions:
    '''
    A class representing the options for a registration form,
    including enumerations for organization names and course identifiers.

    This class provides predefined sets of choices for organizations and
    courses, which can be utilized in the registration form to ensure
    consistency and validity of user selections.
    '''

    course_choices: tuple[tuple[str, str], ...]
    organization_choices: tuple[tuple[str, str], ...]
