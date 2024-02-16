from typing import TYPE_CHECKING

from pytest import fixture

if TYPE_CHECKING:
    from django.contrib.auth.models import AbstractUser


@fixture
def fake_login_credentials() -> dict[str, str]:
    '''Returns information about the fake user'''

    return {
        'first_name': 'John',
        'last_name': 'Snow',
        'email': 'js@mail.ru',
        'username': 'john-snow',
        'password': 'p!ass$word',
    }


@fixture
def fake_account(
    django_user_model: 'AbstractUser',
    fake_login_credentials: dict[str, str]
) -> None:
    '''Adds information about a fake user to the database'''

    django_user_model.objects.create_user(
        username=fake_login_credentials['username'],
        password=fake_login_credentials['password'],
    )
