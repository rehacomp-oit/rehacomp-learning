from dataclasses import dataclass
from typing import final, Self

from server.core.helpers import EntityMixin

from .exceptions import UserCreationError
from .types import UserHashedPassword, UserId
from .validators import validate_email, validate_first_name, validate_last_name


@final
@dataclass(eq=False, init=False, match_args=False, repr=False, slots=True)
class User(EntityMixin):
    '''
    Domain entity representing a user account.

    Note:
        Core domain invariants are enforced at object creation.
    '''

    id: UserId | None  # noqa:VNE003
    first_name: str
    last_name: str
    email: str
    hashed_password: UserHashedPassword


    @property
    def full_name(self) -> str:
        '''
        Returns the employee's full name (first and last name combined).
        '''
        return f'{self.first_name} {self.last_name}'


    @classmethod
    def create(
        cls,
        first_name: str,
        last_name: str,
        email: str,
        hashed_password: UserHashedPassword,
        user_id: int | None = None
    ) -> Self:
        obj = cls()
        obj.id = UserId(user_id) if user_id else None
        try:
            obj.first_name = validate_first_name(first_name)
            obj.last_name = validate_last_name(last_name)
            obj.email = validate_email(email)
        except ValueError as exc:
            raise UserCreationError(str(exc))

        obj.hashed_password = hashed_password
        return obj
