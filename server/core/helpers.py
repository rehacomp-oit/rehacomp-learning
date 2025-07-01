from typing import final, override, Protocol, runtime_checkable, Self


@runtime_checkable
class ComparableID(Protocol):
    def __lt__(self, other: object) -> bool:
        ...

    def __gt__(self, other: object) -> bool:
        ...

    @override
    def __eq__(self, other: object) -> bool:
        ...


class EntityMixin:
    __slots__ = ()

    @override
    def __str__(self) -> str:
        id_repr = getattr(self, 'id')
        return str(id_repr)


    @override
    def __repr__(self) -> str:
        id_repr = getattr(self, 'id')
        return f'<{self.__class__.__name__}({id_repr})>'


    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        else:
            this_id: ComparableID = getattr(self, 'id')
            that_id: ComparableID = getattr(other, 'id')
            return this_id == that_id


    def __lt__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        else:
            this_id: ComparableID = getattr(self, 'id')
            that_id: ComparableID = getattr(other, 'id')
            return this_id < that_id


    def __gt__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        else:
            this_id: ComparableID = getattr(self, 'id')
            that_id: ComparableID = getattr(other, 'id')
            return this_id > that_id


@final
class IntegerId(int):
    __slots__ = ()

    def __new__(cls, value: int) -> Self:
        if not isinstance(value, int):
            raise TypeError('Value must be an integer')
        elif value <= 0:
            raise ValueError('Positive integers only allowed')

        return super().__new__(cls, value)
