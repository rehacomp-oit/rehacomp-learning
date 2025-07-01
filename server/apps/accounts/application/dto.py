from dataclasses import dataclass
from typing import final

from server.apps.accounts.domain import UserHashedPassword, UserRawPassword


@final
@dataclass(frozen=True, slots=True)
class RegisterUserCommand:
    '''
    Structure of the raw source data obtained from signup form.
    '''

    first_name: str
    last_name: str
    email: str
    password1: str
    password2: str


# State objects


@final
@dataclass(frozen=True, slots=True)
class ValidatedInputCarrier:
    first_name: str
    last_name: str
    email: str
    password: UserRawPassword


@final
@dataclass(frozen=True, slots=True)
class PreparedCredentialsCarrier:
    first_name: str
    last_name: str
    email: str
    hashed_password: UserHashedPassword
