from typing import final, TypedDict


class BaseSignUpData(TypedDict):
    first_name: str
    last_name: str
    email: str
    username: str


@final
class RawFormData(BaseSignUpData, total=False):
    password1: str
    password2: str


@final
class RawUserCredentials(BaseSignUpData, total=False):
    '''
    Structure of the raw data of the registered user.
    '''

    raw_password: str
