from typing import final, TypedDict


class BaseSignUpData(TypedDict):
    '''
    a set of basic attributes describing the user's personal data.
    '''

    first_name: str
    last_name: str
    email: str
    username: str


@final
class RawFormData(BaseSignUpData, total=False):
    '''
    Structure of the raw source data obtained from signup form.
    '''

    password1: str
    password2: str


@final
class RawUserCredentials(BaseSignUpData, total=False):
    '''
    Valid user credentials which store into the database during registration.
    '''

    raw_password: str
