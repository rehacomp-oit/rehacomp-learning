from pathlib import Path

from pytest import fixture, mark
from server.utils import load_from_json_file


@fixture
def fake_json(tmpdir) -> tuple[list[int], Path]:
    '''Creates a fake json file with a list of integers.'''

    example = [1, 2, 3, 4, 5, 6]
    file_path = tmpdir.join('example.json')
    with open(file_path, 'w') as file_object:
        file_object.write(str(example))

    return (example, file_path,)


@mark.module
def test_load_from_json_file(fake_json) -> None:
    '''
    this test insures correct deserialization of
    data from the json file.
    '''

    expected_data, file_path = fake_json
    real_data = load_from_json_file(file_path)
    assert len(real_data) == len(expected_data)
    assert real_data == expected_data
