from pytest import mark, raises
from server.apps.accounts.services import create_new_account, ServiceFailed


@mark.django_db
def test_successful_creation(fake_login_credentials: dict[str, str]) -> None:
    '''This test ensures the successful creation of a new account'''

    expected_result = fake_login_credentials['first_name']
    result = create_new_account(**fake_login_credentials)
    assert result == expected_result


def test_create_existing_account(
    fake_account,
    fake_login_credentials: dict[str, str]
) -> None:
    '''This test ensures that it is impossible to register an existing user'''

    with raises(ServiceFailed):
        create_new_account(**fake_login_credentials)


def test_username_case_sensitivity_restrictions(
    fake_account,
    fake_login_credentials: dict[str, str]
) -> None:
    '''
    This test ensures case sensitivity of the username, which
    avoids registering an existing account
    '''

    fake_login_credentials['username'] = fake_login_credentials[
        'username'
    ].upper()
    with raises(ServiceFailed):
        create_new_account(**fake_login_credentials)
