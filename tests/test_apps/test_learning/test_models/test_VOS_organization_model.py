from django.core.exceptions import ValidationError
from pytest import mark, raises
from server.apps.learning.models import VOSOrganization


@mark.module
def test_model_string_representation() -> None:
    '''
    This test ensures that the model is correctly
    converted to a string type
    '''

    expected_value = 'some organization'
    model = VOSOrganization(organization_name=expected_value)
    assert str(model) == expected_value


@mark.module
def test_max_length_constraint(long_random_string) -> None:
    '''
    This test ensures that it is impossible to
    add an entry about an organization
    with a name that is longer than
    80 characters
    '''

    model = VOSOrganization(organization_name=long_random_string(81))
    with raises(ValidationError):
        model.clean_fields()
