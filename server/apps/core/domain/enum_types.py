from typing import final

from server.utilites.common.types import BaseEnum


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
