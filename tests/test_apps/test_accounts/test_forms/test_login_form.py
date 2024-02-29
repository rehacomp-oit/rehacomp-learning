'''
A set of tests for the custom login form object
'''

from typing import Final

import pytest
from server.apps.accounts.forms import LoginForm


FORM_FIELD_NAMES: Final = ('username', 'password',)


@pytest.fixture(scope='module')
def empty_form() -> LoginForm:
    '''Returnes created empty login form'''

    return LoginForm()


@pytest.mark.parametrize('field_name', FORM_FIELD_NAMES)
def test_exists_field(empty_form: LoginForm, field_name: str) -> None:
    '''this test ensures that registration form contains the required field.'''

    field_names = empty_form.fields.keys()
    assert field_name in field_names


def test_auto_focus_username(empty_form: LoginForm) -> None:
    '''
    This test ensures that the <username> field has an autofocus attribute.
    '''

    assert empty_form.fields['username'].widget.attrs['autofocus']


def test_username_max_length(empty_form: LoginForm) -> None:
    '''
    This test ensures that the <username> form field has
    correct maximum number of entered characters.
    '''

    expected_field_length = 10
    field_length = empty_form.fields['username'].widget.attrs['maxlength']
    assert int(field_length) == expected_field_length


def test_username_field_is_required(empty_form: LoginForm) -> None:
    '''This test ensures that the <username> field is required.'''

    assert empty_form.fields['username'].required


def test_form_fields_order(empty_form: LoginForm) -> None:
    '''
    This test ensures that when creating a form, the fields
    are generated in a certain order.
    '''

    expected_fields_order = ('username', 'password',)
    fields_order = tuple(empty_form.fields.keys())
    assert fields_order == expected_fields_order


@pytest.mark.parametrize('field_name', FORM_FIELD_NAMES)
def test_has_label(field_name: str, empty_form: LoginForm) -> None:
    '''This test ensures that the form field has the correct label.'''

    assert empty_form.fields[field_name].label is not None


@pytest.mark.parametrize('field_name', FORM_FIELD_NAMES)
def test_has_help_text(field_name: str, empty_form: LoginForm) -> None:
    '''This test ensures that the form field has the correct label.'''

    assert empty_form.fields[field_name].help_text is not None
