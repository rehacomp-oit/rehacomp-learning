from typing import final, Sequence


@final
class UserCreationError(Exception):
    __slots__ = ()


@final
class DuplicateUserError(Exception):
    __slots__ = ()


@final
class PasswordValidationError(Exception):
    __slots__ = ('exceptions',)

    def __init__(self, validation_result: Sequence[Exception]) -> None:
        super().__init__(validation_result)
        self.exceptions = list(validation_result)
