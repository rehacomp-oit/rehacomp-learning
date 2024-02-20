from typing import final, TYPE_CHECKING

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.password_validation import (
    password_validators_help_text_html
)
from django.core.exceptions import ValidationError
from django.forms import CharField, EmailField, Form, PasswordInput
from django.utils.translation import gettext_lazy as _

if TYPE_CHECKING:
    from django.contrib.auth.models import User  # Noqa: F401


__password_mismatch_error_msg = _('The two password fields didn’t match.')


@final
class RegisterForm(UserCreationForm['User']):

    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )


    first_name = CharField(
        label='Имя',
        help_text='Обязательное поле',
        max_length=20,
        required=True,
    )
    last_name = CharField(
        label='Фамилия',
        help_text='Обязательное поле',
        max_length=20,
        required=True
    )
    email = EmailField(label='Адрес электронной почты', required=True)


    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autofocus'] = False
        self.fields['first_name'].widget.attrs['autofocus'] = True


@final
class _RegisterForm(Form):
    '''
    A form for adding a new user to the system.
    It is used only for rendering the form markup and
    validating received data.
'''

    first_name = CharField(
        label='Имя',
        help_text='Обязательно для заполнения',
        max_length=20,
        required=True,
        strip=True,
    )

    last_name = CharField(
        label='Фамилия',
        help_text='Обязательно для заполнения',
        max_length=20,
        required=True,
        strip=True,
    )

    email = EmailField(
        label='Адрес электронной почты',
        required=True
    )

    username = UsernameField(
        label='Имя пользователя',
        help_text='Обязательно для заполнения',
        max_length=10,
        required=True,
        strip=True,
    )

    password1 = CharField(
        label=_('Password'),
        strip=False,
        widget=PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validators_help_text_html(),
    )

    password2 = CharField(
        label=_('Password confirmation'),
        widget=PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_('Enter the same password as before, for verification.'),
    )


    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True


    def clean_password2(self) -> str | None:
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                __password_mismatch_error_msg,
                code='password_mismatch',
            )

        return password2
