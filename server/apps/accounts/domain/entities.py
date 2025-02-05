from datetime import datetime, timezone
from typing import final, Self

from server.common.domain import Entity
from server.common.helpers import define_entity, define_field

from .value_objects import UserId


@final
@define_entity
class User(Entity):
    id: UserId  # noqa:VNE003
    first_name: str
    last_name: str
    email: str
    date_joined: datetime
    is_active: bool
    last_login: datetime | None = define_field(default=None)


    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'


    @classmethod
    def create_regular_user(cls, first_name: str, last_name: str, email: str) -> Self:
        return User(
            UserId(None),
            first_name,
            last_name,
            email,
            date_joined=datetime.now(tz=timezone.utc),
            is_active=True,
        )
