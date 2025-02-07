from typing import TYPE_CHECKING

from django.contrib.auth import get_user_model
from server.apps.accounts.domain.entities import Employee
from server.common.mappers import domain_to_orm, orm_to_domain

if TYPE_CHECKING:
    from django.contrib.auth.models import AbstractUser


__all__ = ('orm_to_domain', 'domain_to_orm',)

_UserModel = get_user_model()


@orm_to_domain.instance(_UserModel)
def _(model: 'AbstractUser') -> Employee:
    return Employee.frompersistence(
        model.id,
        model.first_name,
        model.last_name,
        model.email,
        model.date_joined
    )


@domain_to_orm.instance(Employee)
def _(entity: Employee) -> 'AbstractUser':
    return _UserModel(
        id=entity.id,
        first_name=entity.first_name,
        last_name=entity.last_name,
        email=entity.email,
        date_joined=entity.date_joined
    )
