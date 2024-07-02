from typing import final

from django.core.exceptions import ValidationError
from pytest import fixture, mark, raises
from server.apps.learning.models import Course, VOSOrganization


@mark.module
@final
class TestCourseModel:

    @fixture
    def invalid_model_object(self, long_random_string) -> Course:
        '''
        Returns an instance of the <Course> model
        with incorrectly entered data.
        '''

        return Course(
            course_name=long_random_string(257),
            course_short_name=long_random_string(11),
        )


    def test_string_representation(self) -> None:
        '''
        This test ensures that the <Course> model is correctly
        converted to a string type.
        '''

        expected_value = 'string2'
        model = Course(course_name='string1', course_short_name='string2')
        assert str(model) == expected_value


    def test_course_name_overflow(self, invalid_model_object: Course):
        with raises(ValidationError):
            invalid_model_object.clean_fields(('course_name',))


    def test_course_short_name_overflow(self, invalid_model_object: Course):
        with raises(ValidationError):
            invalid_model_object.clean_fields(('course_short_name',))


@mark.module
@final
class TestVOSOrganizationModel:

    def test_model_string_representation(self) -> None:
        '''
        This test ensures that the model is correctly
        converted to a string type
        '''

        expected_value = 'some organization'
        model = VOSOrganization(organization_name=expected_value)
        assert str(model) == expected_value


    def test_organization_name_overflow(self, long_random_string) -> None:
        '''
        This test ensures that it is impossible to
        add an entry about an organization
        with a name that is longer than
        80 characters
        '''

        model = VOSOrganization(organization_name=long_random_string(81))
        with raises(ValidationError):
            model.clean_fields()
