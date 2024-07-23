from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse


def test_profile_unauthorized(client: Client) -> None:
    '''This test ensures that profile page requires auth.'''
    response = client.get(reverse('core:profile'))
    assert response.status_code == HTTPStatus.FOUND


def test_profile_authorized(client: Client, django_user_model: User) -> None:
    '''This test ensures that profile page is accessible.'''

    username, password = 'test-user1', 'test-user1'
    test_user = django_user_model.objects.create_user(
        username=username, password=password
    )
    client.force_login(test_user)
    response = client.get(reverse('core:profile'))
    assert response.status_code == HTTPStatus.OK
