'''
A set of tests for the custom registration form object
'''

from typing import Final

from pytest import fixture, mark
from server.apps.accounts.forms import RegisterForm


FORM_FIELD_NAMES: Final = (
    'first_name',
    'last_name',
    'email',
    'username',
    'password1',
    'password2',
)


@fixture(scope='module')
def empty_form() -> RegisterForm:
    '''Returnes created empty registration form'''

    return RegisterForm()


@mark.parametrize('field_name', FORM_FIELD_NAMES)
def test_exists_field(empty_form: RegisterForm, field_name: str) -> None:
    '''this test ensures that registration form contains the required field.'''

    field_names = empty_form.fields.keys()
    assert field_name in field_names


def test_auto_focus_first_name(empty_form: RegisterForm) -> None:
    '''
    This test ensures that the <first_name> field has an autofocus attribute.
    '''

    assert empty_form.fields['first_name'].widget.attrs['autofocus']


@mark.parametrize('field_name', FORM_FIELD_NAMES[:2])
def test_full_name_max_length(
    empty_form: RegisterForm,
    field_name: str
) -> None:
    '''
    This test ensures that <first_name> and <last_name> form fields have
    correct maximum number of entered characters.
    '''

    expected_field_length = 20
    field_length = empty_form.fields[field_name].widget.attrs['maxlength']
    assert int(field_length) == expected_field_length


def test_username_max_length(empty_form: RegisterForm) -> None:
    '''
    This test ensures that <username> form field has
    correct maximum number of entered characters.
    '''

    expected_field_length = 10
    field_length = empty_form.fields['username'].widget.attrs['maxlength']
    assert int(field_length) == expected_field_length


@mark.parametrize('field_name', FORM_FIELD_NAMES)
def test_field_is_required(empty_form: RegisterForm, field_name: str) -> None:
    '''This test ensures that the form field is required.'''

    assert empty_form.fields[field_name].required


@mark.parametrize('field_name', FORM_FIELD_NAMES)
def test_has_label(field_name: str, empty_form: RegisterForm) -> None:
    '''This test ensures that the form field has the correct label.'''

    assert empty_form.fields[field_name].label is not None


@mark.parametrize('field_name', FORM_FIELD_NAMES)
def test_has_help_text(field_name: str, empty_form: RegisterForm) -> None:
    '''This test ensures that the form field has the correct label.'''

    assert empty_form.fields[field_name].help_text is not None


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


def test_not_equal_passwords(fake_login_credentials: dict[str, str]) -> None:
    fake_login_credentials['password2'] = 'qieiojfoqjf'
    form = RegisterForm(fake_login_credentials)
    assert form.has_error('password2')


def test_correct_validation(fake_login_credentials: dict[str, str]) -> None:
    form = RegisterForm(fake_login_credentials)
    assert form.is_valid()
