from typing import Protocol

from returns.result import Result

from .dto import RegisterUserCommand
from .failures import RegistrationFailure


class RegisterUserUsecase(Protocol):
    def execute(self, command: RegisterUserCommand) -> Result[None, RegistrationFailure]:
        ...
