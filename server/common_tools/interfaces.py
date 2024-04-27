from dataclasses import Field
from typing import Any, Protocol


class Entity(Protocol):
    '''Interface of a business entity defined by a dataclass'''

    __dataclass_fields__: dict[str, Field[Any]]
    __match_args__: tuple[str, ...]


class Repository(Protocol):
    '''Interface describing the data warehouse'''

    def save(_: Entity) -> Any:
        ...


def contains(_: Entity) -> bool:
    ...
