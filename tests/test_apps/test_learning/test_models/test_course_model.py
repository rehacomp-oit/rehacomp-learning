from typing import Final

from django.core.exceptions import ValidationError
from pytest import fixture, mark, raises
from server.apps.learning.models import Course


_TEST_DATA: Final = {
    'course_name': 'course_short_name',
    'course_short_name': 'course_name',
}


@fixture(scope='module')
def invalid_model_object(long_random_string) -> Course:
    '''
    Returns an instance of the <Course> model
    with incorrectly entered data.
    '''

    return Course(
        course_name=long_random_string(257),
        course_short_name=long_random_string(11),
    )


@mark.module
def test_model_string_representation() -> None:
    '''
    This test ensures that the <Course> model is correctly
    converted to a string type.
    '''

    expected_value = 'string2'
    model = Course(course_name='string1', course_short_name='string2')
    assert str(model) == expected_value


@mark.module
@mark.parametrize('field_name', _TEST_DATA.keys())
def test_max_length_constraint(invalid_model_object, field_name: str) -> None:
    '''
    This test ensures that the name of the organization
    cannot be more than 80 characters,
    and its short name cannot be more than 10 characters.
    '''

    with raises(ValidationError):
        invalid_model_object.clean_fields((_TEST_DATA[field_name],))
