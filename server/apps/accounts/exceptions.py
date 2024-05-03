from typing import final

from .dto import RawUserCredentials


class SignUpFailure(Exception):
    pass


@final
class MismatchedPasswords(SignUpFailure):

    def __init(self, password1: str, password2: str) -> None:
        super().__init__(f'passwords "{password1}" and "{password2}" do not match!')


@final
class UncorrectPassword(SignUpFailure):

    def __init__(self, invalid_password: str) -> None:
        self.invalid_password = invalid_password
        super().__init__(f'"{invalid_password}" is uncorrect password!')


@final
class AccountAlreadyExists(SignUpFailure):
    def __init__(self, credentials: RawUserCredentials) -> None:
        self.credentials = credentials
        super().__init__(f'user with "{self.credentials.username} already exists!')
