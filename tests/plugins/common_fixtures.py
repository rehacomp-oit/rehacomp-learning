from random import choice
from string import ascii_letters
from typing import Callable

from pytest import fixture


@fixture(scope='module')
def long_random_string() -> Callable[[int], str]:
    '''
    A factory fixture that return a function
    for generation string of random ascii characters
    '''

    return lambda length: ''.join(
        (choice(ascii_letters) for _ in range(length))
    )
