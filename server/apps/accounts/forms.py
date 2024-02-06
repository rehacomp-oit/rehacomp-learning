from typing import final, TYPE_CHECKING

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, EmailField

if TYPE_CHECKING:
    from django.contrib.auth.models import User  # Noqa: F401


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
