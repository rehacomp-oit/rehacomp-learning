from dataclasses import dataclass
from enum import auto, Enum
from typing import Any, final


@final
class RegistrationFailureKind(Enum):
    MISMATCHED_PASSWORDS = auto()
    INVALID_PASSWORD = auto()
    ACCOUNT_ALREADY_EXISTS = auto()
    REGISTRATION_DISABLE = auto()


@final
@dataclass(frozen=True, slots=True)
class RegistrationFailure:
    kind: RegistrationFailureKind
    details: Any = None
