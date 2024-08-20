from typing import final

from hypothesis import given
from hypothesis.strategies import text
from pytest import mark, raises
from server.apps.core.domain.constants import COURSE_FULL_NAME_LENGTH
from server.apps.core.domain.value_objects import CourseFolderName


@final
@mark.module
class TestCourseFolderName:
    '''
    Doc
    '''

    @given(value=text(min_size=1, max_size=COURSE_FULL_NAME_LENGTH))
    def test_success_creation(self, value: str) -> None:
        expected_value = CourseFolderName(value)
        assert expected_value

    def test_empty_string(self) -> None:
        with raises(ValueError):
            CourseFolderName('')


    def test_overflow(self, long_random_string) -> None:
        value = long_random_string(COURSE_FULL_NAME_LENGTH + 1)
        with raises(ValueError):
            CourseFolderName(value)
