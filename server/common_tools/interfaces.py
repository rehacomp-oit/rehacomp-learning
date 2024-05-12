from dataclasses import Field
from typing import Any, Callable, Iterable, Protocol, TypeAlias


RepositoryInput: TypeAlias = 'Entity' | Iterable[Any]
Validator: TypeAlias = Callable[[str], None]


class Entity(Protocol):
    '''Interface of a business entity defined by a dataclass'''

    __dataclass_fields__: dict[str, Field[Any]]
    __match_args__: tuple[str, ...]
    __slots__: tuple[str, ...]


class Repository(Protocol):
    '''Interface describing the data warehouse'''

    def save(self, _: RepositoryInput) -> Any:
        ...


    def contains(self, _: RepositoryInput) -> bool:
        ...
