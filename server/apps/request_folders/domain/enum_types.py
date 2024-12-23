from enum import auto, IntEnum
from typing import final


@final
class TrainingLevel(IntEnum):
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
class DisabilityGroup(IntEnum):
    '''
    Options for possible disability groups.
    '''

    VISION_FIRST = auto()
    VISION_SECOND = auto()
    VISION_THURD = auto()
    OTHER = auto()
    NOTHING = auto()


@final
class LearningRequestStatus(IntEnum):
    REQUEST = auto()
    REJECTION = auto()
