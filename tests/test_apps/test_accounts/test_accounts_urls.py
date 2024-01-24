from typing import Final

from django.urls import resolve
import pytest


URLS: Final = {
    '/accounts/login/': ('login', 'accounts:login'),
    '/accounts/register/': ('register', 'accounts:register'),
}


@pytest.mark.parametrize('route', URLS.keys())
def test_correct_url_name(route: str) -> None:
    expected_url_name = URLS[route][0]
    resolver = resolve(route)
    assert resolver.url_name == expected_url_name


@pytest.mark.parametrize('route', URLS.keys())
def test_correct_view_name(route: str) -> None:
    expected_view_name = URLS[route][1]
    resolver = resolve(route)
    assert resolver.view_name == expected_view_name
