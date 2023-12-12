from http import HTTPStatus

from django.test import Client
from django.urls import reverse


def test_main_page(client: Client) -> None:
    '''This test ensures that main page works.'''
    response = client.get(reverse('index'))
    assert response.status_code == HTTPStatus.OK


def test_profile_page(client: Client) -> None:
    '''This test ensures that profile page works.'''
    response = client.get(reverse('main:profile'))
    assert response.status_code == HTTPStatus.OK
