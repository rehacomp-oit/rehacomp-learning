'''
A set of tests for the custom registration form object
'''

from typing import Final

import pytest
from server.apps.accounts.forms import RegisterForm


FORM_FIELD_NAMES: Final = (
    'first_name',
    'last_name',
    'email',
    'username',
    'password1',
    'password2',
)

FORM_FIELDS_DATA: Final = {
    'first_name': ('Имя', 'Обязательное поле',),
    'last_name': ('Фамилия', 'Обязательное поле',),
    'email': ('Адрес электронной почты',),
}


@pytest.fixture(scope='module')
def empty_form() -> RegisterForm:
    '''Returnes created empty registration form'''

    return RegisterForm()


@pytest.mark.parametrize('field_name', FORM_FIELD_NAMES)
def test_exists_field(empty_form: RegisterForm, field_name: str) -> None:
    '''this test ensures that registration form contains the required field.'''

    field_names = empty_form.fields.keys()
    assert field_name in field_names


def test_auto_focus_first_name(empty_form: RegisterForm) -> None:
    '''
    This test ensures that the <first_name> field has an autofocus attribute.
    '''

    assert empty_form.fields['first_name'].widget.attrs['autofocus']


@pytest.mark.parametrize('field_name', FORM_FIELD_NAMES[:2])
def test_field_max_length(empty_form: RegisterForm, field_name: str) -> None:
    '''
    This test ensures that the form field has
    correct maximum number of entered characters.
    '''

    expected_field_length = 20
    field_length = empty_form.fields[field_name].widget.attrs['maxlength']
    assert int(field_length) == expected_field_length


@pytest.mark.parametrize('field_name', FORM_FIELD_NAMES[:3])
def test_field_is_required(empty_form: RegisterForm, field_name: str) -> None:
    '''This test ensures that the form field is required.'''

    assert empty_form.fields[field_name].required


@pytest.mark.parametrize('field_name', FORM_FIELD_NAMES[:3])
def test_has_label(field_name: str, empty_form: RegisterForm) -> None:
    '''This test ensures that the form field has the correct label.'''

    expected_label = FORM_FIELDS_DATA[field_name][0]
    field_label = empty_form.fields[field_name].label
    assert field_label == expected_label


@pytest.mark.parametrize('field_name', FORM_FIELD_NAMES[:2])
def test_has_help_text(field_name: str, empty_form: RegisterForm) -> None:
    '''This test ensures that the form field has the correct label.'''

    expected_help_text = FORM_FIELDS_DATA[field_name][1]
    help_text = empty_form.fields[field_name].help_text
    assert help_text == expected_help_text


def test_form_fields_order(empty_form: RegisterForm) -> None:
    '''
    This test ensures that when creating a form, the fields
    are generated in a certain order.
    '''

    expected_fields_order = (
        'first_name',
        'last_name',
        'email',
        'username',
        'password1',
        'password2',
    )

    fields_order = tuple(empty_form.fields.keys())
    assert fields_order == expected_fields_order
