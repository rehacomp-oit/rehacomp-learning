from dataclasses import dataclass
from typing import final


@final
@dataclass(slots=True)
class Account:
    '''Defines the account to be registered.'''

    first_name: str
    last_name: str
    email: str
    username: str
    password: str


    @property
    def fool_name(self) -> str:
        return f'{self.first_name} {self.last_name}'
