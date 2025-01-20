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

    return dataclass(eq=False, repr=False, slots=True)(cls)


@dataclass_transform(field_specifiers=(FieldSpeck,))
def define_service(cls: type[_T]) -> type[_T]:
    '''
    A wrapper above the data class used to define service objects.
    '''

    return dataclass(eq=False, frozen=True, slots=True)(cls)
