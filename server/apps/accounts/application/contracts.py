from typing import Protocol

from returns.result import Result
from server.apps.accounts.domain.value_objects import EmployeeHashedPassword, EmployeeRawPassword

from .commands import RegisterEmployeeCommand
from .failure_types import EmployeeRegistrationFailure


class RegisterEmployeeUsecase(Protocol):
    def run(self, command: RegisterEmployeeCommand) -> Result[RegisteredEmployee, EmployeeRegistrationFailure]:
        ...


class PasswordService(Protocol):
    def validate_strength(self, password: EmployeeRawPassword) -> None:
        ...

    def hash_password(self, raw_password: EmployeeRawPassword) -> EmployeeHashedPassword:
        ...
