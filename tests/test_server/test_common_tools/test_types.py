from hypothesis import given
from hypothesis.strategies import integers
from pytest import mark, raises
from server.common_tools.types import BaseEnum, IntegerId


@mark.module
def test_extended_enum_behaviour() -> None:
    '''
    This test ensures that subclass of the base enumeration
    returns a tuple of all values.
    '''

    class Example(BaseEnum):
        AA = 12
        BB = 23
        CC = 34

    expected_result = (12, 23, 34,)
    real_result = Example.get_values()
    assert real_result == expected_result


@mark.module
@given(invalid_data=integers(max_value=0))
def test_integer_id_validation(invalid_data) -> None:
    '''
    This test insures the impossibility to create an integer identifier with a value less than or equal to zero.
    '''

    with raises(ValueError):
        IntegerId(invalid_data)
