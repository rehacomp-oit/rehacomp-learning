from dataclasses import is_dataclass

from pytest import mark
from server.common.helpers import define_entity, define_field, define_service


pytestmark = mark.module


@define_entity
class _SampleEntity:
    name: str = 'test'


@define_service
class _SampleService:
    dependency: str = 'test'


def test_define_entity() -> None:
    entity = _SampleEntity()

    assert is_dataclass(entity)
    assert not hasattr(entity, '__dict__')
    assert hasattr(entity, '__slots__')


def test_define_service() -> None:
    service = _SampleService()

    assert is_dataclass(service)
    assert not hasattr(service, '__dict__')
    assert hasattr(service, '__slots__')


def test_define_field():
    field_instance = define_field(default='test')

    assert field_instance.default == 'test'
    assert not field_instance.compare
    assert not field_instance.repr
