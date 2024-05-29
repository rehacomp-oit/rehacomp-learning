'''
A set of module tests for the custom form objects.
'''

from typing import Final

from pytest import fixture, mark
from server.apps.accounts.forms import LoginForm, RegisterForm


@mark.module
class TestLoginForm:

    _FIELD_NAMES: Final = ('username', 'password',)
    _USERNAME_MAX_LENGTH: Final = 15
    _PASSWORD_MIN_LENGTH: Final = 8


    @fixture(scope='class')
    def unbound_form(self) -> LoginForm:
        '''
        Returnes created unbound login form.
        '''

        return LoginForm()


    @mark.parametrize('field_name', _FIELD_NAMES)
    def test_exists_field(self, unbound_form, field_name: str) -> None:
        '''
        This test ensures that registration form contains the required field.
        '''

        field_names = unbound_form.fields.keys()
        assert field_name in field_names


    def test_success_validation(self, long_random_string) -> None:
        data = {'username': long_random_string(15), 'password': long_random_string(12)}
        form = LoginForm(data)
        assert form.is_valid()


    def test_field_requirements(self) -> None:
        data = {'username': '', 'password': ''}
        form = LoginForm(data)
        assert not form.is_valid()
        assert len(form.errors) == 2
        assert 'username' in form.errors and 'password' in form.errors


    def test_username_max_length(self, long_random_string) -> None:
        '''
        This test ensures that the <username> form field has
        correct maximum number of entered characters.
        '''

        data = {
            'username': long_random_string(self._USERNAME_MAX_LENGTH + 1),
            'password': long_random_string(self._PASSWORD_MIN_LENGTH)
        }
        form = LoginForm(data)
        assert not form.is_valid()
        assert len(form.errors) == 1 and 'username' in form.errors


    def test_password_min_length(self, long_random_string) -> None:
        data = {
            'username': long_random_string(self._USERNAME_MAX_LENGTH),
            'password': long_random_string(self._PASSWORD_MIN_LENGTH - 1)
        }
        form = LoginForm(data)
        assert not form.is_valid()
        assert len(form.errors) == 1 and 'password' in form.errors


    def test_fields_order(self, unbound_form) -> None:
        '''
        This test ensures that when creating a form, the fields
    are generated in a certain order.
        '''

        fields_order = tuple(unbound_form.fields.keys())
        assert fields_order == self._FIELD_NAMES


@mark.module
class TestRegisterForm:

    _FIELD_NAMES: Final = (
        'first_name',
        'last_name',
        'email',
        'username',
        'password1',
        'password2',
    )
    _REAL_NAME_MAX_LENGTH: Final = 20
    _USERNAME_MAX_LENGTH: Final = 15
    _PASSWORD_MIN_LENGTH: Final = 8


    @fixture
    def unbound_form(self) -> RegisterForm:
        return RegisterForm()


    @mark.parametrize('field_name', _FIELD_NAMES)
    def test_exists_field(self, unbound_form, field_name: str) -> None:
        '''this test ensures that registration form contains the required field.'''

        field_names = unbound_form.fields.keys()
        assert field_name in field_names


    def test_success_validation(self, fake_login_credentials) -> None:
        form = RegisterForm(fake_login_credentials)
        assert form.is_valid()


    def test_field_requirements(self) -> None:
        data = {'first_name': '', 'last_name': '', 'email': '', 'username': '', 'password1': '', 'password2': ''}
        form = RegisterForm(data)
        assert not form.is_valid()
        assert len(form.errors) == 6


    def test_passwords_min_length(self, fake_login_credentials, long_random_string) -> None:
        fake_login_credentials['password1'] = long_random_string(self._PASSWORD_MIN_LENGTH - 1)
        fake_login_credentials['password2'] = long_random_string(self._PASSWORD_MIN_LENGTH - 1)
        form = RegisterForm(fake_login_credentials)
        assert not form.is_valid()
        assert len(form.errors) == 2 and ('password1' in form.errors and 'password2' in form.errors)


    def test_username_max_length(self, fake_login_credentials, long_random_string) -> None:
        fake_login_credentials['username'] = long_random_string(self._USERNAME_MAX_LENGTH + 1)
        form = RegisterForm(fake_login_credentials)
        assert not form.is_valid()
        assert len(form.errors) == 1 and 'username' in form.errors



    def test_real_names_max_length(self, fake_login_credentials, long_random_string) -> None:
        fake_login_credentials['first_name'] = long_random_string(self._REAL_NAME_MAX_LENGTH + 1)
        fake_login_credentials['last_name'] = long_random_string(self._REAL_NAME_MAX_LENGTH + 1)
        form = RegisterForm(fake_login_credentials)
        assert not form.is_valid()
        assert len(form.errors) == 2
        assert 'first_name' in form.errors and 'last_name' in form.errors


    def test_fields_order(self, unbound_form) -> None:
        '''
        This test ensures that when creating a form, the fields
    are generated in a certain order.
        '''

        fields_order = tuple(unbound_form.fields.keys())
        assert fields_order == self._FIELD_NAMES
