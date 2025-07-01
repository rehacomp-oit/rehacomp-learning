from enum import StrEnum
from typing import final


@final
class AccountsTemplate(StrEnum):
    LOGIN = 'accounts/login.html'
    REGISTER = 'accounts/register.html'
    PROFILE = 'accounts/profile.html'
