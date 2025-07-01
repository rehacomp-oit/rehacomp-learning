from dataclasses import dataclass
from typing import Any, final

from returns.pipeline import flow
from returns.pointfree import bind
from returns.result import Failure, Result, Success
from server.apps.accounts.domain import (
    DuplicateUserError,
    PasswordValidationError,
    User,
    UserCreationError,
    UserPasswordManager,
    UserRawPassword,
    UserRepository
)

from .dto import (
    PreparedCredentialsCarrier,
    RegisterUserCommand,
    ValidatedInputCarrier
)
from .failures import RegistrationFailure, RegistrationFailureKind


def _fail(
    kind: RegistrationFailureKind,
    details: Any=None
) -> Failure[RegistrationFailure]:
    return Failure(RegistrationFailure(kind=kind, details=details))


@final
@dataclass(eq=False, frozen=True, slots=True)
class RegisterUserUsecaseImpl:
    '''Creates new account.'''

    user_repo: UserRepository
    password_manager: UserPasswordManager


    def execute(
        self,
        cmd: RegisterUserCommand
    ) -> Result[None, RegistrationFailure]:
        return flow(
            cmd,
            self._validate_input,
            bind(self._hash_password),
            bind(self._create_account),
            bind(self._persist_account)
        )


    def _validate_input(
        self,
        cmd: RegisterUserCommand
    ) -> Result[ValidatedInputCarrier, RegistrationFailure]:
        if cmd.password1 != cmd.password2:
            return Failure(RegistrationFailure(
                kind=RegistrationFailureKind.MISMATCHED_PASSWORDS
            ))

        try:
            self.password_manager.validate_password_strength(cmd.password2)
        except PasswordValidationError as exc:
            return Failure(RegistrationFailure(
                kind=RegistrationFailureKind.INVALID_PASSWORD,
                details=exc.exceptions
            ))

        return Success(ValidatedInputCarrier(
            cmd.first_name,
            cmd.last_name,
            cmd.email,
            UserRawPassword(cmd.password2)
        ))


    def _hash_password(
        self,
        state: ValidatedInputCarrier
    ) -> Success[PreparedCredentialsCarrier]:
        password_hash = self.password_manager.hash_password(state.password)
        return Success(PreparedCredentialsCarrier(
            state.first_name,
            state.last_name,
            state.email,
            password_hash
        ))


    def _create_account(
        self,
        state: PreparedCredentialsCarrier
    ) -> Result[User, RegistrationFailure]:
        try:
            user = User.create(
                first_name=state.first_name,
                last_name=state.last_name,
                email=state.email,
                hashed_password=state.hashed_password
            )
        except UserCreationError as exc:
            return Failure(RegistrationFailure(
                kind=RegistrationFailureKind.REGISTRATION_DISABLE,
                details=exc
            ))

        return Success(user)


    def _persist_account(
        self,
        created_user: User
    ) -> Result[None, RegistrationFailure]:
        try:
            self.user_repo.add(created_user)
        except DuplicateUserError:
            return Failure(RegistrationFailure(
                kind=RegistrationFailureKind.ACCOUNT_ALREADY_EXISTS
            ))

        return Success(None)
