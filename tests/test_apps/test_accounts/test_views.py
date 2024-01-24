from http import HTTPStatus

from django.test import Client


def test_register_user_view(client: Client) -> None:
    '''This test ensures that Sign Up page works.'''
    response = client.get('/accounts/register/')
    assert response.status_code == HTTPStatus.OK


def test_login_user_view(client: Client) -> None:
    '''This test ensures that login page works.'''
    response = client.get('/accounts/login/')
    assert response.status_code == HTTPStatus.OK
