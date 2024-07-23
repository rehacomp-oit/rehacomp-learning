from typing import Final, final

from django.core.exceptions import ValidationError
from pytest import fixture, mark, raises
from server.apps.core.models import Course, VOSOrganization


@mark.module
@final
class TestCourseModel:
    '''
    A set of unit tests for a model describing the training course.
    '''

    FULL_NAME_LENGTH: Final = 256
    SHORT_NAME_LENGTH: Final = 10

    @fixture
    def invalid_model_object(self, long_random_string) -> Course:
        '''
        Returns an instance of the <Course> model
        with incorrectly entered data.
        '''

        return Course(
            course_name=long_random_string(self.FULL_NAME_LENGTH + 1),
            course_short_name=long_random_string(self.SHORT_NAME_LENGTH + 1),
        )


    def test_string_representation(self) -> None:
        '''
        This test ensures that the <Course> model is correctly converting to a string type.
        '''

        expected_value = 'string2'
        model = Course(course_name='string1', course_short_name='string2')
        assert str(model) == expected_value


    def test_course_name_overflow(self, invalid_model_object: Course):
        '''
        This test ensures that the full name of the course cannot be stored in more than 256 characters.
        '''

        with raises(ValidationError):
            invalid_model_object.clean_fields(('course_name',))


    def test_course_short_name_overflow(self, invalid_model_object: Course):
        '''
        This test ensures that the abbreviation of the course name cannot be stored in more than 10 characters.
        '''

        with raises(ValidationError):
            invalid_model_object.clean_fields(('course_short_name',))


@mark.module
@final
class TestVOSOrganizationModel:
    '''
    A set of unit tests for a model describing the <VOS> organization.
    '''

    ORGANIZATION_NAME_LENGTH: Final = 80


    def test_string_representation(self) -> None:
        '''
        This test ensures that the <VOSOrganization> model is correctly converting to a string type.
        '''

        expected_value = 'some organization'
        model = VOSOrganization(organization_name=expected_value)
        assert str(model) == expected_value


    def test_organization_name_overflow(self, long_random_string) -> None:
        '''
        This test ensures that the name of the organization cannot be stored in more than 80 characters.
        '''

        new_length = self.ORGANIZATION_NAME_LENGTH + 1
        model = VOSOrganization(organization_name=long_random_string(new_length))
        with raises(ValidationError):
            model.clean_fields()
