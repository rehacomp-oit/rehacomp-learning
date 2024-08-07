from dataclasses import dataclass, field
from typing import final

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db.models import Q

from .dto_types import RawUserCredentials


@final
@dataclass(frozen=True, slots=True)
class DatabaseRepository:
    __Model: AbstractUser = field(default_factory=get_user_model)

    def save(self, credentials: RawUserCredentials) -> None:
        new_user = self.__Model(
            first_name=credentials['first_name'],
            last_name=credentials['last_name'],
            email=credentials['email'],
            username=credentials['username']
        )
        new_user.set_password(credentials['raw_password'])
        new_user.save()


    def contains(self, credentials: RawUserCredentials) -> bool:
        username = credentials['username']
        filter_condition = Q(username=username) | Q(username__iexact=username)
        return self.__Model.objects.filter(filter_condition).exists()
