from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


def validate_password_format(raw_password: str) -> None:
    try:
        validate_password(password=raw_password)
    except ValidationError as error:
        raise ValueError(error.message)
