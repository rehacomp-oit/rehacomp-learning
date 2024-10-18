from typing import final

from server.common.types import BaseEnum


@final
class TrainingLevels(int, BaseEnum):
    '''
    Options for possible levels of computer or smartphone proficiency.
    '''

    ZERO = 0
    BEGINNER = 1
    BASIC = 2
    CONFIDENT = 3
    EXPERIENCED = 4
    ADVANCED = 5


@final
class DisabilityGroups(int, BaseEnum):
    '''
    Options for possible disability groups.
    '''

    VISION_FIRST = 1
    VISION_SECOND = 2
    VISION_THURD = 3
    OTHER = 4
    NOTHING = 5
