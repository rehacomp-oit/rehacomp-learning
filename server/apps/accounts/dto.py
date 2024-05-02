from typing import final, NamedTuple


@final
class RawUserCredentials(NamedTuple):
    '''
    Structure of the raw data of the registered user.
    '''

    first_name: str
    last_name: str
    email: str
    username: str
    raw_password: str
