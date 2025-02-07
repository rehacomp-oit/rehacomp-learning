from dataclasses import dataclass
from datetime import datetime
from typing import final, Self

from server.common.helpers import EntityMixin

from .exceptions import InvalidEmployee
from .value_objects import EmployeeEmail, EmployeeId, EmployeePersonName


@final
@dataclass(eq=False, init=False, match_args=False, repr=False, slots=True)
class Employee(EntityMixin):
    '''
    Domain entity representing a company employee.

    Note:
        Use classmethod `create` for constructing new valid domain objects.
        Core domain invariants are enforced at object creation.
    '''

    first_name: EmployeePersonName
    last_name: EmployeePersonName
    email: EmployeeEmail
    date_joined: datetime
    # None for employees not yet persisted in storage
    id: EmployeeId | None = None  # noqa:VNE003


    @property
    def full_name(self) -> str:
        '''
        Returns the employee's full name (first and last name combined).
        '''
        return f'{self.first_name} {self.last_name}'


    @classmethod
    def create(
        cls,
        first_name: str,
        last_name: str,
        email: str,
        date_joined: datetime
    ) -> Self:
        '''
        Factory method for creating a new Employee entity.

        All invariants are checked, and domain-specific exceptions are raised.

        Args:
            first_name: Employee first name.
            last_name: Employee last name.
            email: Employee email address.
            date_joined: When the employee joined.

        Returns:
            Employee: A new Employee instance.

        Raises:
            InvalidEmployee: If any attribute fails domain validation.
        '''
        try:
            first_name_VO = EmployeePersonName(first_name)
            last_name_VO = EmployeePersonName(last_name)
            email_VO = EmployeeEmail(email)
        except ValueError as exc:
            raise InvalidEmployee(str(exc))

        if date_joined > datetime.now():
            raise InvalidEmployee('Employee join date cannot be in the future')

        obj = super().__new__(cls)
        obj.first_name = first_name_VO
        obj.last_name = last_name_VO
        obj.email = email_VO
        obj.date_joined = date_joined
        return obj


    @classmethod
    def frompersistence(
        cls,
        id: int,  # noqa:VNE003
        firstname: str,
        lastname: str,
        email: str,
        datejoined: datetime
    ) -> Self:
        obj = super().__new__(cls)
        obj.id, obj.email = id, email
        obj.first_name, obj.last_name = firstname, lastname
        obj.date_joined = datejoined
        return obj
