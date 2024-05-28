# Todo: refactor these tests
from pytest import fixture, mark, raises
from server.apps.accounts.logic.dto_types import RawFormData, RawUserCredentials
from server.apps.accounts.logic.exceptions import AccountAlreadyExists, MismatchedPasswords, UncorrectPassword
from server.apps.accounts.logic.services import SignUpService


class CredentialsMockRepository:
    def __init__(self) -> None:
        self.__storage: list[RawUserCredentials] = []


    def save(self, credentials: RawUserCredentials) -> None:
        self.__storage.append(credentials)


    def contains(self, credentials: RawUserCredentials) -> bool:
        for record in self.__storage:
            if credentials['username'].lower() == record['username'].lower():
                return True
        else:
            return False


@fixture
def fake_signup_data() -> RawFormData:
    return {
        'first_name': 'john',
        'last_name': 'snow',
        'email': 'john@yandex.ru',
        'username': 'john-snow',
        'password1': 'password',
        'password2': 'password'
    }


@fixture
def service() -> SignUpService:
    return SignUpService(CredentialsMockRepository(), lambda password: None)


@fixture
def service2() -> SignUpService:
    def validate_password(password: str):
        raise ValueError

    return SignUpService(CredentialsMockRepository(), validate_password)


@fixture
def service3(fake_signup_data) -> SignUpService:
    fake_credentials = fake_signup_data.copy()
    fake_credentials['raw_password'] = fake_signup_data['password1']
    del fake_credentials['password1'], fake_credentials['password2']
    repository = CredentialsMockRepository()
    repository.save(fake_credentials)
    return SignUpService(repository, lambda password: None)


@mark.module
def test_successful_signup(fake_signup_data: RawFormData, service: SignUpService) -> None:
    service(fake_signup_data)
    assert 2 > 1


@mark.module
def test_signup_with_mismatched_passwords(fake_signup_data, service: SignUpService) -> None:
    fake_signup_data['password2'] = 'test'
    with raises(MismatchedPasswords):
        service(fake_signup_data)


@mark.module
def test_signup_with_wrong_password(fake_signup_data, service2: SignUpService) -> None:
    with raises(UncorrectPassword) as error:
        service2(fake_signup_data)
        assert error.value.invalid_password == fake_signup_data['password1']


@mark.module
def test_tmp(fake_signup_data: RawFormData, service3: SignUpService) -> None:
    with raises(AccountAlreadyExists):
        service3(fake_signup_data)
