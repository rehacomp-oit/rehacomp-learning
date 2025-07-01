from __future__ import annotations

from typing import final, TYPE_CHECKING

from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.db.models import Q
from server.apps.accounts.domain import DuplicateUserError, User, UserHashedPassword

if TYPE_CHECKING:
    from .orm_models import User as UserModel


@final
class DjangoUserRepository:
    '''
    Concrete repository implementation for User entity using Django ORM.
    '''
    __slots__ = ('__model')

    def __init__(self) -> None:
        self.__model: type[UserModel] = get_user_model()


    def add(
        self,
        new_user: User
    ) -> User:
        '''
        See repository protocol.

        Persists a new user in the database using Django ORM.
        Converts the domain entity to ORM model and stores it.
        '''

        user = self._to_orm(new_user)
        try:
            user.save()
            return self._to_domain(user)
        except IntegrityError as exc:
            raise DuplicateUserError from exc


    def exists_by_email(self, email: str) -> bool:
        '''
        See repository protocol.

        Checks the database for presence of an user with the specified email using Django ORM.
        Returns True if found, otherwise False.
        '''

        filter_condition = Q(email=email) | Q(email__iexact=email)
        return self.__model.objects.filter(filter_condition).exists()


    def _to_orm(self, entity: User) -> UserModel:
        return self.__model(
            first_name=entity.first_name,
            last_name=entity.last_name,
            email=entity.email,
            password=entity.hashed_password
        )


    def _to_domain(self, model: UserModel) -> User:
        return User.create(
            first_name=model.first_name,
            last_name=model.last_name,
            email=model.email,
            hashed_password=UserHashedPassword(model.password),
            user_id=model.id
        )
