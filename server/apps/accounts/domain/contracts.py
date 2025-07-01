from typing import Protocol

from .entities import User
from .types import UserHashedPassword, UserRawPassword


class UserRepository(Protocol):
    '''
    Repository interface for managing User account entities.
    '''

    def add(
        self,
        new_user: User
    ) -> User:
        '''
        Persists a new User account in the repository.
        '''
        ...


    def exists_by_email(self, email: str) -> bool:
        ...


class UserPasswordManager(Protocol):
    def validate_password_strength(self, password: str) -> None:
        ...


    def hash_password(self, source: UserRawPassword) -> UserHashedPassword:
        ...
