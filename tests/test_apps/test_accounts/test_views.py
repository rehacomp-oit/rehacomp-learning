from http import HTTPStatus

from django.test import Client
from django.urls import reverse


def test_register_user_view(client: Client) -> None:
    '''This test ensures that Sign Up page works.'''
    response = client.get(reverse('register'))
    assert response.status_code == HTTPStatus.OK


def test_login_user_view(client: Client) -> None:
    '''This test ensures that login page works.'''
    response = client.get(reverse('login'))
    assert response.status_code == HTTPStatus.OK
