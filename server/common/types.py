from enum import Enum
from typing import Any, NewType


FailureReason = NewType('FailureReason', str)


class BaseEnum(Enum):
    '''
    Extends built-in Enumeration With New Behavior.
    it is used as a base class when defining enumerations.
    '''

    @classmethod
    def get_values(cls) -> tuple[Any, ...]:
        return tuple(item.value for item in cls.__members__.values())
