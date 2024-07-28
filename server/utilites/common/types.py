from enum import Enum
from typing import Any, final, Self


class BaseEnum(Enum):
    '''
    Extends built-in Enumeration With New Behavior.
    it is used as a base class when defining enumerations.
    '''

    @classmethod
    def get_values(cls) -> tuple[Any, ...]:
        return tuple(item.value for item in cls.__members__.values())


@final
class IntegerId(int):
    '''
    A type that allows you to create identifiers in the form of positive integers.
    It must be used instead of the integer type built into python.
    '''

    def __new__(cls, value: int) -> Self:
        if value <= 0:
            raise ValueError('Value must be a positive integer')
        else:
            return super().__new__(cls, value)
