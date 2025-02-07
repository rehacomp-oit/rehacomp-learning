from dataclasses import dataclass, replace
from logging import getLogger
from typing import final

from returns.pipeline import flow
from returns.pointfree import bind
from returns.result import Failure, Result, Success


from .commands import RegisterEmployeeCommand
from .contracts import EmployeeRepository, PasswordService
from .exceptions import InvalidPassword
from .failure_types import EmployeeRegistrationFailure, PasswordValidationError, RegistrationFailureReason
from ..domain.entities import ProspectiveEmployee, RegisteredEmployee
from ..domain.value_objects import EmployeePassword


_logger = getLogger(__name__)


@final
@dataclass(frozen=True, slots=True)
class _RegistrationState:
    command: RegisterEmployeeCommand
    password: EmployeePassword | None = None
    hashed_password: str | None = None
    employee: ProspectiveEmployee | None = None


@final
@dataclass(eq=False, frozen=True, slots=True)
class RegisterEmployeeService:
    '''Creates new account.'''

    # Dependencies:
    employee_repo: EmployeeRepository
    password_service: PasswordService


    def run(self, command: RegisterEmployeeCommand) -> Result[RegisteredEmployee, EmployeeRegistrationFailure]:
        _logger.info('Starting registration process for email: %s', command.email)
        return flow(
            _RegistrationState(command),
            self._extract_valid_password,
            bind(self._validate_password_strength),
            bind(self._ensure_employee_does_not_exist),
            bind(self._create_employee_account),
            bind(self._encrypt_password),
            bind(self._save_employee_account)
        )


    def _extract_valid_password(
        self,
        state: _RegistrationState
    ) -> Result[_RegistrationState, EmployeeRegistrationFailure]:
        password, password_confirmation = state.command.password1, state.command.password2
        if password != password_confirmation:
            _logger.warning(
                'Password mismatch for email: %s. Passwords do not match.',
                state.command.email
            )
            return Failure(RegistrationFailureReason.MISMATCHED_PASSWORDS)
        else:
            return Success(replace(state, password=EmployeePassword(password)))


    def _validate_password_strength(
        self,
        state: _RegistrationState
    ) -> Result[_RegistrationState, EmployeeRegistrationFailure]:
        try:
            self.password_service.validate_strength(state.password)
        except InvalidPassword as error:
            _logger.error(
                'Invalid password. Reason: %s',
                str(error)
            )
            return Failure(PasswordValidationError(error.validation_messages))
        else:
            return Success(state)


    def _encrypt_password(
        self,
        state: _RegistrationState
    ) -> Result[_RegistrationState, EmployeeRegistrationFailure]:
        password_hash = self.password_service.hash_password(state.password)
        return Success(replace(state, hashed_password=password_hash))


    def _ensure_employee_does_not_exist(
        self,
        state: _RegistrationState
    ) -> Result[_RegistrationState, EmployeeRegistrationFailure]:
        email = state.command.email
        if self.employee_repo.exists_by_email(email):
            _logger.warning('Employee with email: %s already exists', email)
            return Failure(RegistrationFailureReason.EMPLOYEE_ALLREADY_EXISTS)
        else:
            return Success(state)


    def _create_employee_account(
        self,
        state: _RegistrationState
    ) -> Result[_RegistrationState, EmployeeRegistrationFailure]:
        first_name, last_name = state.command.first_name, state.command.last_name
        email = state.command.email
        new_employee = ProspectiveEmployee.create(email, first_name, last_name)
        return Success(replace(state, employee=new_employee))


    def _save_employee_account(
        self,
        state: _RegistrationState
    ) -> Result[RegisteredEmployee, EmployeeRegistrationFailure]:
        saved_employee = self.employee_repo.add(state.employee, state.hashed_password)
        _logger.debug('Employee saved successfully with email: %s and ID: %s', saved_employee.email, saved_employee.id)
        return Success(saved_employee)
