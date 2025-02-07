from dataclasses import dataclass
from typing import final


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
