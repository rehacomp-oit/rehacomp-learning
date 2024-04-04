from json import dump
from pathlib import Path
from typing import Any, final, Iterable

from pytest import fixture
from server.apps.common.services import CreateInitialDataDumpService


@final
class MockQueryManager:
    '''
    A fake queryset manager object that implements
    the method of multiple record insertion.
    '''

    def bulk_create(self, bucket: Iterable[Any]) -> None:
        pass


@final
class MockVOSOrganization:
    '''The fake model of the VOS organization'''

    objects: MockQueryManager = MockQueryManager()

    def __init__(self, organization_name) -> None:
        self.organization_name = organization_name


@final
class MockCourse:
    '''Fake object of the course model.'''

    objects: MockQueryManager = MockQueryManager()

    def __init(self, course_name, course_short_name) -> None:
        self.course_name = course_name
        self.course_short_name = course_short_name


@fixture
def fake_input_file(tmpdir, long_random_string) -> Path:
    '''Creates a json file with fake data.'''

    new_file_path = tmpdir.join('example.json')

    data = {
        'courses': [
            {'course_name': 'course1', 'course_short_name': 'cr1'},
            {'course_name': 'course2', 'course_short_name': 'cr2'},
            {'course_name': 'course3', 'course_short_name': 'cr3'},
            {'course_name': 'course4', 'course_short_name': 'cr4'},
        ],
        'vos': [
            {'organization_name': 'organization1'},
            {'organization_name': 'organization2'},
            {'organization_name': 'organization3'},
            {'organization_name': 'organization4'},
            {'organization_name': 'organization5'},
        ],
    }

    with open(new_file_path, 'w') as file_object:
        dump(data, file_object)

    return new_file_path


def test_create_initial_data_dump_service(fake_input_file) -> None:
    '''
    This test insures the correct operation of this service with
    fake model objects.
    '''

    service = CreateInitialDataDumpService(
        MockCourse,
        MockVOSOrganization
    )
    assert service(fake_input_file)
