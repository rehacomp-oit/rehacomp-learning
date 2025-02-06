from typing import final

from server.common.domain import EntityId


@final
class UserId(EntityId):
    __slots__ = EntityId.__slots__
