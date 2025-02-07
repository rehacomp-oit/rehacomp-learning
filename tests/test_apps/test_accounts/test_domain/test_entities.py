from datetime import timezone

from pytest import mark
from server.apps.accounts.domain.entities import Employee


@mark.module
class TestEmployee:

    def test_create_anonymous_employee(self) -> None:
        email = 'test@example.com'
        new_employee = Employee.create(email)

        assert new_employee.id is None
        assert new_employee.email == email
        assert not new_employee.first_name
        assert not new_employee.last_name
        assert new_employee.is_active
        assert new_employee.date_joined.tzinfo == timezone.utc
        assert new_employee.last_login is None


    def test_create_regular_employee(self) -> None:
        email = 'test@example.com'
        first_name, last_name = 'test1', 'test2'
        test_employee = Employee.create(email, first_name, last_name,)

        assert test_employee.id is None
        assert test_employee.email == email
        assert test_employee.first_name == first_name
        assert test_employee.last_name == last_name
        assert test_employee.is_active
        assert test_employee.date_joined.tzinfo == timezone.utc
        assert test_employee.last_login is None


    @mark.parametrize(
        'first_name, last_name, real_full_name',
        (
            ('John', '', 'John',),
            ('', 'Doe', 'Doe',),
            ('John', 'Doe', 'John Doe',)
        ),
    )
    def test_full_name(self, first_name: str, last_name: str, real_full_name: str) -> None:
        email = 'test@example.com'
        test_employee = Employee.create(email, first_name, last_name)
        assert test_employee.full_name == real_full_name


    def test_full_name_for_anonymous(self) -> None:
        email = 'test@example.com'
        test_employee = Employee.create(email)

        assert not test_employee.full_name
        assert test_employee.full_name == ''
