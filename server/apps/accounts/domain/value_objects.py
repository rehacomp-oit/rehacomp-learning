from re import compile as re_compile
from re import IGNORECASE
from typing import ClassVar, final, NewType, Self

from server.apps.accounts.constants import EMPLOYEE_EMAIL_MAX_LENGTH, EMPLOYEE_NAME_MAX_LENGTH


@final
class EmployeePersonName(str):
    '''
    Value object representing a person's first or last name.

    - Strips leading and trailing whitespaces.
    - Must not be empty or exceed a maximum length.
    - May be used for both first_name and last_name.
    '''

    def __new__(cls, value: str) -> Self:
        value = value.strip()
        if not value:
            raise ValueError('Person name cannot be empty')

        if len(value) > EMPLOYEE_NAME_MAX_LENGTH:
            raise ValueError('Person  name too long')

        return super().__new__(cls, value)


@final
class EmployeeEmail(str):
    '''
    Value object for employee email address.

    - Strips input and applies a regex-based RFC-compliant validation.
    - Maximum length controlled by constants.
    - Email format validation is kept similar to Django's EmailField, but independent.
    '''

    _REGEX: ClassVar = re_compile(
        r'(^[-!#$%&\'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&\'*+/=?^_`{}|~0-9A-Z]+)*'
        r'|^"([^"\r\\]|\\.)+"'
        r')@([A-Z0-9-]+\.)+[A-Z]{2,}$',
        IGNORECASE
    )

    def __new__(cls, value: str) -> Self:
        value = value.strip()
        if not value:
            raise ValueError('Email address required')

        if len(value) > EMPLOYEE_EMAIL_MAX_LENGTH:
            raise ValueError('Email address too long')

        if not cls._REGEX.match(value):
            raise ValueError('Email format invalid')

        return super().__new__(cls, value)


@final
class EmployeeRawPassword(str):
    '''
    Value object for a new employee's password in plain text.

    - Enforces password length bounds only.
    - Does not perform checks for password strength or prohibited characters;
      these are to be handled outside of the domain layer.
    - When printed or repr'd, replaces value with asterisks for safety.
    '''

    MIN_LENGTH: ClassVar[int] = 8
    MAX_LENGTH: ClassVar[int] = 128


    def __new__(cls, value: str) -> Self:
        value = value.strip() or ''
        if not (cls.MIN_LENGTH <= len(value) <= cls.MAX_LENGTH):
            raise ValueError(f'Password must be between {cls.MIN_LENGTH} and {cls.MAX_LENGTH} characters')

        return super().__new__(cls, value)


    def __repr__(self) -> str:
        placeholder = '*' * len(self)
        return f'RawPassword({placeholder})'


EmployeeId = NewType('EmployeeId', int)
EmployeeHashedPassword = NewType('EmployeeHashedPassword', str)
