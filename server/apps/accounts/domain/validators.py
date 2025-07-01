from re import compile as re_compile

from . import constants


_email_basic_re = re_compile(
    r'^[^@\s]+@[^@\s]+\.[^@\s]+'
)


def validate_first_name(value: str) -> str:
    min_length = constants.USER_MIN_NAME_LENGTH
    max_length = constants.USER_MAX_NAME_LENGTH
    clean_value = value.strip()
    if not (min_length <= len(clean_value) <= max_length):
        raise ValueError(
            f'First name must be between {min_length} and {max_length} chars'
        )

    return clean_value


def validate_last_name(value: str) -> str:
    min_length = constants.USER_MIN_NAME_LENGTH
    max_length = constants.USER_MAX_NAME_LENGTH
    clean_value = value.strip()
    if not (min_length <= len(clean_value) <= max_length):
        raise ValueError(
            f'Last name must be between {min_length} and {max_length} chars'
        )

    return clean_value


def validate_email(value: str) -> str:
    email_length = constants.USER_EMAIL_MAX_LENGTH
    clean_value = value.strip()
    if len(clean_value) > email_length:
        raise ValueError(f'Email too long (max {email_length})')

    try:
        email_name, domain_part = clean_value.rsplit('@', 1)
    except ValueError:
        pass
    else:
        clean_value = f'{email_name}@{domain_part.lower()}'

    if not _email_basic_re.match(clean_value):
        raise ValueError('Invalid email format')

    return clean_value
