from typing import Any, final

from django.core.exceptions import ValidationError
from django.forms import CharField, EmailField, Form, PasswordInput
from django.utils.translation import gettext_lazy as _
from server.apps.accounts.application import RegisterUserCommand
from server.apps.accounts.domain import (
    USER_EMAIL_MAX_LENGTH,
    USER_MAX_NAME_LENGTH,
    USER_MIN_NAME_LENGTH,
    USER_PASSWORD_MAX_LENGTH,
    USER_PASSWORD_MIN_LENGTH
)


_password_widget = PasswordInput(
    attrs={'autocomplete': 'password'}
)


@final
class SignupForm(Form):
    '''
    A custom form for adding a new user to the system.
    It is used only for rendering the form markup and
    validating received data.
'''

    first_name = CharField(
        max_length=USER_MAX_NAME_LENGTH,
        min_length=USER_MIN_NAME_LENGTH,
        required=True,
        strip=True
    )

    last_name = CharField(
        max_length=USER_MAX_NAME_LENGTH,
        min_length=USER_MIN_NAME_LENGTH,
        required=True,
        strip=True
    )

    email = EmailField(
        max_length=USER_EMAIL_MAX_LENGTH,
        required=True
    )

    password1 = CharField(
        min_length=USER_PASSWORD_MIN_LENGTH,
        max_length=USER_PASSWORD_MAX_LENGTH,
        strip=False,
        widget=_password_widget
    )

    password2 = CharField(
        min_length=USER_PASSWORD_MIN_LENGTH,
        max_length=USER_PASSWORD_MAX_LENGTH,
        strip=False,
        widget=_password_widget
    )


    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True


    @property
    def output(self) -> RegisterUserCommand:
        return RegisterUserCommand(**self.cleaned_data)


    def set_mismatched_passwords_error(self) -> None:
        self.add_error(
            'password2',
            _('The two entered passwords didn\'t match.')
        )


    def set_account_already_exists_error(self) -> None:
        self.add_error(
            'email',
            _('User with this email address already exists.')
        )


    def set_password_validation_error(
        self,
        errors: list[Exception]
    ) -> None:
        reason = ValidationError(errors)
        super().add_error('password2', reason)
