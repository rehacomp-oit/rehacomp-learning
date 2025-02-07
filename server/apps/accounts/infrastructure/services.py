from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import get_default_password_validators
from django.core.exceptions import ValidationError
from server.apps.accounts.application.exceptions import InvalidPassword
from server.apps.accounts.domain.value_objects import (
    EmployeeHashedPassword,
    EmployeePassword,
    EmployeeValidatedPassword
)


def validate_password_strength(password: EmployeePassword) -> EmployeeValidatedPassword:
    validators = get_default_password_validators()
    error_messages = []
    for validator in validators:
        try:
            validator.validate(password)
        except ValidationError as exc:
            error_messages.append(exc.message)

    if error_messages:
        raise InvalidPassword(error_messages)
    else:
        return EmployeeValidatedPassword(password)


def hash_password(raw_password: EmployeeValidatedPassword) -> EmployeeHashedPassword:
    password_hesh = make_password(str(raw_password))
    return EmployeeHashedPassword(password_hesh)
