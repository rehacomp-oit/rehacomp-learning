from dataclasses import dataclass, field
from typing import final

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.db.models import Q

from .dto import RawUserCredentials
from .entities import UserId


@final
@dataclass(frozen=True, slots=True)
class UserRepository:
    __Model: AbstractBaseUser = field(default_factory=get_user_model)

    def save(self, credentials: RawUserCredentials) -> UserId:
        transformed_credentials = credentials._asdict()
        password = transformed_credentials.pop('raw_password')
        new_user = self.__Model(**transformed_credentials)
        new_user.set_password(password)
        new_user.save()
        return UserId(new_user.pk)


    def contains(self, credentials: RawUserCredentials) -> bool:
        filter_condition = Q(username=credentials.username) | Q(username__iexact=credentials.username)
        return self.__Model.objects.filter(filter_condition).exists()
