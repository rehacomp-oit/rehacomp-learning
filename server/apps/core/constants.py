from typing import Final, final

from server.common_tools.types import BaseEnum


VOS_ORGANIZATION_NAME_LENGTH: Final = 80

COURSE_FULL_NAME_LENGTH: Final = 256
COURSE_SHORT_NAME_LANGTH: Final = 10

EMAIL_ADDRESS_PATTERN: Final = r'^\S+@\S+\.\S+$'
PHONE_NUMBER_PATTERN: Final = r'^\+7\(\d{3}\)\d{3}\-\d{2}\-\d{2}$'
PHONE_NUMBER_MAX_LENGTH: Final = 20
# A person's first name, patronymic and last name have the same number of characters.
PERSON_NAME_LENGTH: Final = 20
DISABILITY_GROUP_LENGTH: Final = 5
EDUCATION_INFORMATION_LENGTH: Final = 80
JOB_INFORMATION_LENGTH: Final = 80


@final
class TrainingLevels(int, BaseEnum):
    '''Options for possible levels of computer or smartphone proficiency.'''

    ZERO = 0
    BEGINNER = 1
    BASIC = 2
    CONFIDENT = 3
    EXPERIENCED = 4
    ADVANCED = 5


@final
class DisabilityGroups(str, BaseEnum):
    '''Options for possible disability groups.'''

    VISION_FIRST = 'v1'
    VISION_SECOND = 'v2'
    VISION_THURD = 'v3'
    OTHER = 'o'
    NOTHING = 'n'
