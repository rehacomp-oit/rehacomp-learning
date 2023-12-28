from http import HTTPStatus

from django.test import Client
from django.urls import resolve
import pytest


@pytest.mark.django_db()
def test_health_check(client: Client) -> None:
    '''This test ensures that health check is accessible.'''

    response = client.get('/health/')
    assert response.status_code == HTTPStatus.OK


def test_admin_unauthorized(client: Client) -> None:
    '''This test ensures that admin panel requires auth.'''

    response = client.get('/admin/')
    assert response.status_code == HTTPStatus.FOUND


def test_admin_authorized(admin_client: Client) -> None:
    '''This test ensures that admin panel is accessible.'''

    response = admin_client.get('/admin/')
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize('page', (
    '/robots.txt',
    '/humans.txt',
))
def test_specials_txt(client: Client, page: str) -> None:
    '''This test ensures that special `txt` files are accessible.'''

    response = client.get(page)
    assert response.status_code == HTTPStatus.OK
    assert response.get('Content-Type') == 'text/plain'


def test_index_url(client: Client) -> None:
    '''This test ensures that index url is accessible.'''

    expected_view_function_name = 'index'
    resolver = resolve('/')
    assert resolver.func.__name__ == expected_view_function_name
    response = client.get('/')
    assert response.status_code != HTTPStatus.NOT_FOUND
