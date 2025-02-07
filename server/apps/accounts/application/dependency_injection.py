from punq import Container

from .protocols import RegisterEmployeeUsecase
from .services import RegisterEmployeeService
from ..domain.protocols import (
    EmployeeEmailChecker,
    EmployeePasswordSaver,
    EmployeeSaver,
    PasswordHasher,
    PasswordValidator
)
from ..infrastructure.repositories import exists_employee_by_email, save_employee, save_password_for_employee
from ..infrastructure.utilits import hash_password, validate_password


register_employee_container = Container()
register_employee_container.register(PasswordValidator, instance=validate_password)
register_employee_container.register(PasswordHasher, instance=hash_password)
register_employee_container.register(EmployeeEmailChecker, instance=exists_employee_by_email)
register_employee_container.register(EmployeePasswordSaver, instance=save_password_for_employee)
register_employee_container.register(EmployeeSaver, instance=save_employee)
register_employee_container.register(RegisterEmployeeUsecase, RegisterEmployeeService)
