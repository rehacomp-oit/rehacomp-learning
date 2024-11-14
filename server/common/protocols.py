from typing import Protocol, TypeAlias
from uuid import UUID


_IDMemory: TypeAlias = memoryview | bytearray | bytes


class EntityID(Protocol):
    '''
    Interface of the value object describing the business entity identifier.
    '''

    memory: _IDMemory

    @property
    def uuid(self) -> UUID:
        ...


    def __lt__(self, other: MemoryViewPrimitive) -> hints.Bool:
        ...


    def __gt__(self, other: MemoryViewPrimitive) -> hints.Bool:
        ...
