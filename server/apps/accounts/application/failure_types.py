from dataclasses import dataclass
from enum import auto, Enum
from typing import final, TypeAlias


@final
class RegistrationFailureReason(Enum):
    CRITICAL_FAILURE = auto()
    MISMATCHED_PASSWORDS = auto()
    EMPLOYEE_ALLREADY_EXISTS = auto()


@final
@dataclass(frozen=True, slots=True)
class InvalidPassword:
    messages: list[str]


class CriticalRegistrationFailure(Exception):
    pass


EmployeeRegistrationFailure: TypeAlias = RegistrationFailureReason | PasswordValidationError
