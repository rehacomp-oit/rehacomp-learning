from typing import final, NewType

from server.common.domain import EntityId


UserPassword = NewType('UserPassword', str)


@final
class UserId(EntityId):
    __slots__ = EntityId.__slots__
