from dataclasses import Field
from typing import Any, Iterable, Protocol, TypeAlias


class Entity(Protocol):
    '''Interface of a business entity defined by a dataclass'''

    __dataclass_fields__: dict[str, Field[Any]]
    __match_args__: tuple[str, ...]
    __slots__: tuple[str, ...]


_RepositoryInput: TypeAlias = Entity | Iterable[Any]


class Repository(Protocol):
    '''Interface describing the data warehouse'''

    def save(self, _: _RepositoryInput) -> Any:
        ...


    def contains(self, _: _RepositoryInput) -> bool:
        ...
