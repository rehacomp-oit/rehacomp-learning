from typing import Callable, Protocol, TypeAlias

from .dto_types import RawUserCredentials


PasswordValidator: TypeAlias = Callable[[str], None]


class UserCredentialsRepository(Protocol):
    '''
    Interface describing a repository for storing user's registration data.
    '''

    def save(self, credentials: RawUserCredentials) -> None:
        ...


    def contains(self, credentials: RawUserCredentials) -> bool:
        ...
