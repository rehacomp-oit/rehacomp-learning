from typing import Protocol

from ..domain.entities import User
from ..domain.value_objects import UserId


class UserRepository(Protocol):
    def add(self, user: User, raw_password: str) -> UserId:
        ...

    def contains(self, user: User) -> bool:
        ...
