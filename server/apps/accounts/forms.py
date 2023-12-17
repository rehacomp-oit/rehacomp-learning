from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, EmailField


class SignupForm(UserCreationForm[User]):

    class Meta(UserCreationForm.Meta):
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
