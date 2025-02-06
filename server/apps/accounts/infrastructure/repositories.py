from dataclasses import asdict
from typing import final, TYPE_CHECKING

from django.contrib.auth import get_user_model
from django.db.models import Q

from ..domain.entities import User
from ..domain.value_objects import UserId

if TYPE_CHECKING:
    from django.contrib.auth.models import AbstractBaseUser


@final
class UserDjangoRepository:
    __slots__ = ('_model',)
    _model: AbstractBaseUser

    def __init__(self) -> None:
        self._model = get_user_model()


    def add(self, user: User, raw_password: str) -> UserId:
        user_object = self._model(**asdict(user))
        user_object.set_password(raw_password)
        user_object.save()
        return UserId(user_object.id)


    def contains(self, user: User) -> bool:
        email = user.email
        filter_condition = Q(email=email) | Q(email__iexact=email)
        return self._model.objects.filter(filter_condition).exists()
