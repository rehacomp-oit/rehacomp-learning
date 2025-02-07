from dataclasses import dataclass, field
from dataclasses import Field as FieldSpeck
from functools import partial
from typing import dataclass_transform, TypeVar


_T = TypeVar('_T')


# Shortcut for more convenient definition of fields in domain objects
define_field = partial(
    field, compare=False, init=False, repr=False
)


@dataclass_transform(field_specifiers=(FieldSpeck,))
def define_entity(cls: type[_T]) -> type[_T]:
    '''
    A wrapper above the data class used to define domain entities.
    '''

    return dataclass(eq=False, match_args=False, repr=False, slots=True)(cls)


@dataclass_transform(field_specifiers=(FieldSpeck,))
def define_service(cls: type[_T]) -> type[_T]:
    '''
    A wrapper above the data class used to define service objects.
    '''

    return dataclass(eq=False, frozen=True, slots=True)(cls)


class EntityMixin:
    __slots__ = ()

    def __str__(self) -> str:
        id_repr = getattr(self, 'id')
        return str(id_repr)


    def __repr__(self) -> str:
        id_repr = getattr(self, 'id')
        return f'<{self.__class__.__name__}({id_repr})>'


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        else:
            return getattr(self, 'id') == getattr(other, 'id')


    def __lt__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        else:
            return getattr(self, 'id') < getattr(other, 'id')


    def __gt__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        else:
            return getattr(self, 'id') > getattr(other, 'id')
