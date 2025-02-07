from typing import final


@final
class MismatchedPasswords(Exception):
    __slots__ = ('field', 'reason',)

    def __init__(self) -> None:
        message = 'The two password fields didn\'t match.'
        super().__init__(message)
        self.reason = message
        self.field = 'password2'


@final
class InvalidPassword(Exception):
    __slots__ = ('field', 'validation_messages',)

    def __init__(self, validation_messages: list[str]) -> None:
        super().__init__(validation_messages)
        self.validation_messages = validation_messages


@final
class EmployeeAlreadyExists(Exception):
    __slots__ = ('field', 'reason',)

    def __init__(self) -> None:
        message = 'The employee with such an email already exists!'
        super().__init__(message)
        self.reason = message
