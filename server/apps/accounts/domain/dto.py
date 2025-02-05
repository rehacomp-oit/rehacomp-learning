from typing import final, TypedDict


@final
class RawSignupFormData(TypedDict):
    '''
    Structure of the raw source data obtained from signup form.
    '''

    first_name: str
    last_name: str
    email: str
    password1: str
    password2: str
