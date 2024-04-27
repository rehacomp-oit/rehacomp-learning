from dataclasses import dataclass
from typing import final, TypeAlias

from server.common_tools.types import IntegerId


UserId: TypeAlias = IntegerId


@final
@dataclass(slots=True)
class Account:
    '''Defines the account to be registered.'''

    account_id: UserId
    first_name: str
    last_name: str
    email: str
    username: str


    @property
    def fool_user_name(self) -> str:
        return f'{self.first_name} {self.last_name}'
