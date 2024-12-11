from typing import final, NewType

from server.common.domain import EntityId


CourseId = NewType('CourseId', EntityId)
OrganizationId = NewType('OrganizationId', EntityId)


@final
class OrganizationCode:
    '''
    Represents a value object for an organization code.

    The organization code is a positive integer that uniquely identifies an organization.

    :raises TypeError: If the provided value is not an integer.
    :raises ValueError: If the provided value is not a positive integer.
    '''
    __slots__ = ('__code')

    def __init__(self, code: int) -> None:
        if not isinstance(code, int):
            raise TypeError('Organization\'s code must be an integer!')

        if code <= 0:
            raise ValueError('Organization\'s code must be a positive integer!')

        self.__code = code


    def __str__(self) -> str:
        return str(self.__code)


    @property
    def code(self) -> int:
        return self.__code


    def __repr__(self):
        return f'OrganizationCode({self.__code})'


    def __int__(self) -> int:
        return self.__code


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, OrganizationCode):
            return NotImplemented

        return self.__code == other.__code


    def __hash__(self) -> int:
        return hash(self.__code)
