from abc import ABC
from enum import Enum
from typing import Any, final, NewType, Self

from ulid import ULID

from .exceptions import InvalidIdentifier


FailureReason = NewType('FailureReason', str)


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
            raise InvalidIdentifier(value)
        else:
            return super().__new__(cls, value)


class EntityId:
    __slots__ = ('__value')
    __value: Any


    def __init__(self, value: Any) -> None:
        self.__value = value


    def __str__(self) -> str:
        return str(self.__value)


    @property
    def value(self) -> Any:
        return self.__value


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EntityId):
            return NotImplemented
        else:
            return self.__value == other.__value


    def __lt__(self, other: object) -> bool:
        if not isinstance(other, EntityId):
            return NotImplemented
        else:
            return self.__value < other.__value


    def __gt__(self, other: object) -> bool:
        if not isinstance(other, EntityId):
            return NotImplemented
        else:
            return self.__value > other.__value



class BaseEntity(ABC):
    '''
    base entity implementation
    '''

    id: ULID  # noqa: VNE003


    def __str__(self) -> str:
        return str(self.id)


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BaseEntity):
            return NotImplemented
        else:
            return self.id == other.id


    def __lt__(self, other: object) -> bool:
        if not isinstance(other, BaseEntity):
            return NotImplemented
        else:
            return self.id < other.id


    def __gt__(self, other: object) -> bool:
        if not isinstance(other, BaseEntity):
            return NotImplemented
        else:
            return self.id > other.id
