from typing import final

from django.forms import CharField, EmailField, Form, PasswordInput

from .application.dto import RawSignupFormData


@final
class SignupForm(Form):
    '''
    A custom form for adding a new user to the system.
    It is used only for rendering the form markup and
    validating received data.
'''

    first_name = CharField(max_length=20, required=True, strip=True)
    last_name = CharField(max_length=20, required=True, strip=True)
    email = EmailField(required=True)
    password1 = CharField(min_length=8, strip=False, widget=PasswordInput(attrs={'autocomplete': 'password'}))
    password2 = CharField(min_length=8, strip=False, widget=PasswordInput(attrs={'autocomplete': 'password'}))


    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True


    @property
    def output(self) -> RawSignupFormData:
        return RawSignupFormData(**self.cleaned_data)
