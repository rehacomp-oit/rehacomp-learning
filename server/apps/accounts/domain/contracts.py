from typing import Protocol

from .entities import Employee
from .value_objects import EmployeeEmail, EmployeeHashedPassword


class EmployeeRepository(Protocol):
    '''
    Repository interface for managing Employee entities.

    All methods may raise RepositoryError on critical infrastructure failures.
    '''

    def add(self, employee: Employee, hashed_password: EmployeeHashedPassword) -> Employee:
        '''
        Persists a new Employee in the repository.

        Args:
            employee: The Employee entity to be stored.
            hashed_password: The Employee's hashed password value object.

        Returns:
            The stored Employee entity (could be updated with repository-generated data).

        Raises:
            RepositoryError: If the repository operation fails.
        '''
        ...


    def exists_by_email(self, email: EmployeeEmail) -> bool:
        '''
        Checks whether an Employee with the given email exists in the repository.

        Args:
            email: Email to lookup.

        Returns:
            True if an Employee with this email exists, False otherwise.

        Raises:
            RepositoryError: If the repository operation fails.
        '''
        ...
