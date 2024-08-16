'''
Test cases for all url patterns in this application
'''

from collections import namedtuple
from typing import Final

from django.urls import resolve
from pytest import mark


# Datastructure for storing the related information with url address
UrlMetadata = namedtuple(
    'UrlMetadata',
    ('url_name', 'view_name',),
)


URL_PATTERN_FIXTURE: Final = {
    '/': UrlMetadata('index', 'index'),
    '/main/': UrlMetadata('home', 'main:home'),
    '/accounts/login/': UrlMetadata('login', 'accounts:login'),
    '/accounts/logout/': UrlMetadata('logout', 'accounts:logout'),
    '/accounts/register/': UrlMetadata('register', 'accounts:register'),
    '/learning_requests/': UrlMetadata('requests', 'learning_requests:requests'),
}


@mark.parametrize('route', URL_PATTERN_FIXTURE.keys())
def test_correct_url_name(route: str) -> None:
    '''this test ensures that the url is mapped to the correct url name'''

    expected_url_name = URL_PATTERN_FIXTURE[route].url_name
    resolver = resolve(route)
    assert resolver.url_name == expected_url_name


@mark.parametrize('route', URL_PATTERN_FIXTURE.keys())
def test_correct_view_name(route: str) -> None:
    '''this test ensures that the url is mapped to the correct view name'''

    expected_view_name = URL_PATTERN_FIXTURE[route].view_name
    resolver = resolve(route)
    assert resolver.view_name == expected_view_name


def test_resolve_index() -> None:
    '''
    This test ensures that the profile url and the root url
    refer to the same view function
    '''

    profile_url_resolver = resolve('/main/')
    index_url_resolver = resolve('/')
    assert index_url_resolver.func is profile_url_resolver.func
