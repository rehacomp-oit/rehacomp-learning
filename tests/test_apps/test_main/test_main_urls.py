from typing import Final

from django.urls import resolve
import pytest


URLS: Final = {
    '/': ('index', 'index'),
    '/main/profile/': ('profile', 'main:profile'),
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


def test_resolve_index() -> None:
    '''
    This test ensures that the profile url and the root url
    refer to the same view function
    '''

    profile_url_resolver = resolve('/main/profile/')
    index_url_resolver = resolve('/')
    assert index_url_resolver.func is profile_url_resolver.func
