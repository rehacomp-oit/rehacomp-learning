from typing import final

from django.contrib.auth import get_user_model
from django.db import DatabaseError
from django.db.models import Q
from server.apps.accounts.domain.entities import Employee
from server.apps.accounts.domain.value_objects import EmployeeEmail, EmployeeHashedPassword
from server.apps.accounts.exceptions import RepositoryError

from .mappers import domain_to_orm, orm_to_domain


_UserModel = get_user_model()


@final
class DjangoEmployeeRepository:
    '''
    Concrete repository implementation for Employee entity using Django ORM.
    '''
    __slots__ = ()


    def add(self, employee: Employee, hashed_password: EmployeeHashedPassword) -> Employee:
        '''
        See repository protocol.

        Persists a new Employee in the database using Django ORM.
        Converts the domain entity to ORM model and stores it.
        Raises RepositoryError if a database error occurs.
        '''
        user = domain_to_orm(employee)
        user.password = hashed_password
        try:
            user.save()
        except DatabaseError as exc:
            raise RepositoryError('Failed to create employee') from exc

        return orm_to_domain(user)


    def exists_by_email(self, email: EmployeeEmail) -> bool:
        '''
        See repository protocol.

        Checks the database for presence of an employee with the specified email using Django ORM.
        Returns True if found, otherwise False.
        Raises RepositoryError on database errors.
        '''
        filter_condition = Q(email=email) | Q(email__iexact=email)
        try:
            return _UserModel.objects.filter(filter_condition).exists()
        except DatabaseError as exc:
            raise RepositoryError('Failed to check employee existence') from exc
