from typing import final

from django.contrib.auth import get_user_model
from django.db.models import Q


__User = get_user_model()


@final
class ServiceFailed(Exception):
    '''Unsuccessful execution of a business scenario'''

    pass


def create_new_account(
        first_name: str,
        last_name: str,
        email: str,
        username: str,
        password: str,
) -> str:
    '''
    Registers a new user in the system.
    when trying to register an existing account
    raises a <Service Failed> exception
    '''

    filter_condition = Q(username=username) | Q(username__iexact=username)
    if __User.objects.filter(filter_condition).exists():
        raise ServiceFailed('Attempt to create an existing user')

    new_user = __User(username=username, email=email)
    new_user.first_name = first_name
    new_user.last_name = last_name
    new_user.set_password(password)
    new_user.save()
    return new_user.first_name
