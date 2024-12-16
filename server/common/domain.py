from abc import ABC
from dataclasses import dataclass, field
from functools import partial
from typing import Any, dataclass_transform, final, TypeVar


__all__ = (
    'define_entity',
    'EntityId',
    'Entity',
)


_T = TypeVar('_T')

entity_field = partial(field, compare=False, init=False, repr=False)


@dataclass_transform()
def define_entity(cls: type[_T]) -> type[_T]:
    '''
    Configures the standard dataclass by disabling the comparison methods and enabling slots.
    '''

    return dataclass(eq=False, repr=False, slots=True)(cls)


@final
class EntityId:
    '''
    Value object for domain identifiers.

    This abstraction allows you to implement ID generation as isolated as possible.
    '''

    __slots__ = ('__value')
    __value: Any


    def __init__(self, value: Any) -> None:
        self.__value = value


    def __str__(self) -> str:
        return str(self.__value)


    @property
    def value(self) -> Any:
        return self.__value


    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}({self.__value})>'


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


class Entity(ABC):
    '''
    base entity implementation
    '''

    # A small optimization has been applied here to reduce the size of child classes
    __slots__ = ()
    id: EntityId  # noqa: VNE003


    def __str__(self) -> str:
        return str(self.id)


    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}({self.id})>'


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Entity):
            return NotImplemented
        else:
            return self.id == other.id


    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Entity):
            return NotImplemented
        else:
            return self.id < other.id


    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Entity):
            return NotImplemented
        else:
            return self.id > other.id
