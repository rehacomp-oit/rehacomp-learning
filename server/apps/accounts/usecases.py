from dataclasses import dataclass
from typing import cast, final

from server.common_tools.interfaces import Repository, Validator

from .dto_types import RawFormData, RawUserCredentials
from .exceptions import AccountAlreadyExists, MismatchedPasswords, UncorrectPassword


@final
@dataclass(frozen=True, slots=True)
class SignUp:
    '''Creates new account.'''

    # Dependencies.

    _storage: Repository
    _validate_password: Validator


    def __call__(self, source: RawFormData) -> None:
        raw_password = self._compare_passwords(source)
        raw_password = cast(str, raw_password)
        self._validate_password_strength(raw_password)
        credentials = self._prepair_user_credentials(source, raw_password)
        self._check_account_existence(credentials)
        self._persist_account(credentials)


    def _compare_passwords(self, source_data: RawFormData) -> str | None:
        password1 = source_data.get('password1')
        password2 = source_data.get('password2')
        if password1 != password2:
            raise MismatchedPasswords(password1, password2)
        else:
            return password1


    def _validate_password_strength(self, raw_password: str) -> None:
        try:
            self._validate_password(raw_password)
        except ValueError:
            raise UncorrectPassword(raw_password)


    def _prepair_user_credentials(self, source_data: RawFormData, validated_password: str) -> RawUserCredentials:
        source_data = source_data.copy()
        del source_data['password1'], source_data['password2']
        credentials = cast(RawUserCredentials, source_data)
        credentials['raw_password'] = validated_password
        return credentials


    def _check_account_existence(self, credentials: RawUserCredentials) -> None:
        if not self._storage.contains(credentials):
            raise AccountAlreadyExists(credentials)


    def _persist_account(self, credentials: RawUserCredentials) -> None:
        self._storage.save(credentials)
