from typing import final, TypeAlias
from unittest.mock import Mock

from django.core.exceptions import ValidationError
from pytest import fixture, mark, MonkeyPatch, raises
from server.common import django_tools


PKULIDField: TypeAlias = django_tools.PKULIDField


@mark.module
@final
class TestPKULIDField:
    '''
    A set of unit tests for ULID django model field.
    '''

    @fixture
    def fake_field_instance(self) -> PKULIDField:
        return django_tools.PKULIDField()


    def test_max_length(self, fake_field_instance: PKULIDField) -> None:
        expected_length = 26
        assert fake_field_instance.max_length == expected_length


    def test_get_internal_type(self, fake_field_instance: PKULIDField) -> None:
        expected_type_name = 'UUIDField'
        actual_type_name = fake_field_instance.get_internal_type()
        assert actual_type_name == expected_type_name


    def test_from_db_value(self, fake_field_instance: PKULIDField) -> None:
        expected_value = 'Hellow, world!'
        setattr(fake_field_instance, 'to_python', Mock(return_value=expected_value))
        actual_value = fake_field_instance.from_db_value(None, None, None)
        assert actual_value == expected_value


    def test_to_python_successful(self, fake_field_instance: PKULIDField, monkeypatch: MonkeyPatch) -> None:
        expected_result = 'Hello, world!'
        monkeypatch.setattr(django_tools, 'parse', lambda string: expected_result)
        actual_result = fake_field_instance.to_python('')
        assert actual_result == expected_result


    def test_to_python_failed(self, fake_field_instance: PKULIDField, monkeypatch: MonkeyPatch) -> None:
        def funk(value):
            raise ValueError

        monkeypatch.setattr(django_tools, 'parse', funk)
        with raises(ValidationError):
            fake_field_instance.to_python('')
