from enum import auto, IntEnum
from typing import final

from server.common.types import BaseEnum


@final
class TrainingLevel(int, BaseEnum):
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
class DisabilityGroup(int, BaseEnum):
    '''
    Options for possible disability groups.
    '''

    VISION_FIRST = 1
    VISION_SECOND = 2
    VISION_THURD = 3
    OTHER = 4
    NOTHING = 5


@final
class LearningRequestStatus(IntEnum):
    REQUEST = auto()
    REJECTION = auto()
