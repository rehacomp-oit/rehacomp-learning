from django.contrib.auth import get_user_model
from django.db.models import Q
from server.exceptions import ServiceFailed


__User = get_user_model()


def create_new_account(raw_form_data: dict[str, str]) -> str:
    '''
    Registers a new user in the system.
    when trying to register an existing account
    raises a <Service Failed> exception
    '''

    filter_condition = Q(
        username=raw_form_data['username']
    ) | Q(
        username__iexact=raw_form_data['username']
    )
    if __User.objects.filter(filter_condition).exists():
        raise ServiceFailed('Attempt to create an existing user')

    new_user = __User(
        username=raw_form_data['username'],
        email=raw_form_data['email']
    )
    new_user.first_name = raw_form_data['first_name']
    new_user.last_name = raw_form_data['last_name']
    new_user.set_password(raw_form_data['password1'])
    new_user.save()
    return new_user.first_name
