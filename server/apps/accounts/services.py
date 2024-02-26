from typing import final, TypedDict

from django.contrib.auth import get_user_model
from django.db.models import Q
from server.exceptions import ServiceFailed


__User = get_user_model()


@final
class _RegisterFormData(TypedDict):
    first_name: str
    last_name: str
    email: str
    username: str
    password1: str
    password2: str


def create_new_account(source: _RegisterFormData) -> str:
    '''
    Registers a new user in the system.
    when trying to register an existing account
    raises a <Service Failed> exception
    '''

    filter_condition = Q(
        username=source['username']
    ) | Q(
        username__iexact=source['username']
    )
    if __User.objects.filter(filter_condition).exists():
        raise ServiceFailed('Attempt to create an existing user')

    new_user = __User(username=source['username'], email=source['email'])
    new_user.first_name = source['first_name']
    new_user.last_name = source['last_name']
    new_user.set_password(source['password1'])
    new_user.save()
    return new_user.first_name
