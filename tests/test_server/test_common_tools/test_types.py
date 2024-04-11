from server.common_tools.types import BaseEnum


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
