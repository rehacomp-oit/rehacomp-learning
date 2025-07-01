from typing import final

from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import get_default_password_validators
from django.core.exceptions import ValidationError
from server.apps.accounts.domain import (
    PasswordValidationError,
    UserHashedPassword,
    UserRawPassword
)


@final
class DjangoUserPasswordManager:
    def validate_password_strength(self, password: str) -> None:
        errors = []
        for validator in get_default_password_validators():
            try:
                validator.validate(password)
            except ValidationError as exc:
                errors.append(exc)

        if errors:
            raise PasswordValidationError(errors)


    def hash_password(self, source: UserRawPassword) -> UserHashedPassword:
        password_hesh = make_password(source)
        return UserHashedPassword(password_hesh)
