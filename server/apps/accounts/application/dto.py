from dataclasses import dataclass
from typing import final

from server.apps.accounts.domain.value_objects import EmployeeHashedPassword, EmployeeRawPassword


@final
@dataclass(frozen=True, slots=True)
class RegisterEmployeeCommand:
    '''
    Structure of the raw source data obtained from signup form.
    '''

    first_name: str
    last_name: str
    email: str
    password1: str
    password2: str


@final
@dataclass(frozen=True, slots=True)
class PasswordValidatedCarrier:
    command: RegisterEmployeeCommand
    password: EmployeeRawPassword


@final
@dataclass(frozen=True, slots=True)
class HashedPasswordCarrier:
    command: RegisterEmployeeCommand
    password: EmployeeHashedPassword
