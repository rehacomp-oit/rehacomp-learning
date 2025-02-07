from dataclasses import replace

from pytest import fixture, mark
from pytest_mock import MockerFixture
from returns.result import Failure, Success
from server.apps.accounts.application.dto import RawSignupFormData
from server.apps.accounts.application.services import RegisterEmployeeService
from server.apps.accounts.domain.entities import Employee
from server.apps.accounts.domain.exceptions import EmployeeAlreadyExists, InvalidPassword, MismatchedPasswords


pytestmark = mark.module


@fixture(name='dependencies')
def construct_mock_dependencies(mocker: MockerFixture):
    return {
        'save_employee': mocker.MagicMock(side_effect=lambda emp: emp),
        'save_password': mocker.MagicMock(),
        'exists_employee': mocker.MagicMock(return_value=False),
        'validate_password': mocker.MagicMock(),
        'hash_password': mocker.MagicMock(return_value='hashed'),
    }


@fixture(name='valid_employee_data')
def construct_employee_data() -> RawSignupFormData:
    return RawSignupFormData(
        email='test@example.com',
        password1='P@ssword123',
        password2='P@ssword123',
        first_name='Test',
        last_name='User',
    )


def test_success_registration(dependencies, valid_employee_data) -> None:
    service = RegisterEmployeeService(**dependencies)
    result = service(valid_employee_data)

    assert isinstance(result, Success)
    assert isinstance(result.unwrap(), Employee)


def test_register_with_mismatched_passwords(dependencies, valid_employee_data) -> None:
    service = RegisterEmployeeService(**dependencies)
    valid_employee_data = replace(valid_employee_data, password2='uncorrect_password')
    result = service(valid_employee_data)

    assert isinstance(result, Failure)
    assert isinstance(result.failure(), MismatchedPasswords)


def test_register_existed_employee(dependencies, valid_employee_data) -> None:
    dependencies['exists_employee'].return_value = True
    service = RegisterEmployeeService(**dependencies)
    result = service(valid_employee_data)

    assert isinstance(result, Failure)
    assert isinstance(result.failure(), EmployeeAlreadyExists)


def test_registration_with_invalid_password(dependencies, valid_employee_data) -> None:
    dependencies['validate_password'].side_effect = InvalidPassword(['message'])
    service = RegisterEmployeeService(**dependencies)
    result = service(valid_employee_data)

    assert isinstance(result, Failure)
    assert isinstance(result.failure(), InvalidPassword)


def test_hash_password_called(dependencies, valid_employee_data) -> None:
    service = RegisterEmployeeService(**dependencies)
    service(valid_employee_data)

    service.hash_password.assert_called_once_with(  # type: ignore[attr-defined]
        valid_employee_data.password1
    )


def test_save_employee_called(dependencies, valid_employee_data) -> None:
    service = RegisterEmployeeService(**dependencies)
    service(valid_employee_data)

    assert service.save_employee.called  # type: ignore[attr-defined]
    assert isinstance(
        service.save_employee.call_args[0][0],  # type: ignore[attr-defined]
        Employee
    )


def test_save_password_called(dependencies, valid_employee_data) -> None:
    service = RegisterEmployeeService(**dependencies)
    result = service(valid_employee_data)

    service.save_password.assert_called_once_with(  # type: ignore[attr-defined]
        result.unwrap().id,
        'hashed'
    )
