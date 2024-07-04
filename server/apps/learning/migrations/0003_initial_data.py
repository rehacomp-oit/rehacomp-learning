from json import load
from pathlib import Path
from typing import Final, TypeAlias

from django.apps.registry import Apps
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations import Migration as BaseMigration
from django.db.migrations import RunPython


SOURCE_FILENAME: Final = 'initial_data.json'
SOURCE_FILE_PATH: Final = Path(__file__).parent.joinpath(SOURCE_FILENAME)
APP_NAME: Final = 'learning'

_DataDump: TypeAlias = dict[str, list[dict[str, str]]]


def load_dump(file_path: Path) -> _DataDump:
    '''
    Returns deserialized data from a json file.
    '''

    with open(file_path) as file_object:
        return load(file_object)


def insert_prepared_data(apps: Apps, _: BaseDatabaseSchemaEditor) -> None:
    '''
    Adds prepared information about courses and VOS organizations to the database.
    '''

    source_data = load_dump(SOURCE_FILE_PATH)
    Course = apps.get_model(APP_NAME, 'Course')
    VOSOrganization = apps.get_model(APP_NAME, 'VOSOrganization')
    Course.objects.bulk_create((Course(**record) for record in source_data['courses']))
    VOSOrganization.objects.bulk_create((VOSOrganization(**record) for record in source_data['VOS']))


def remove_prepared_data(apps: Apps, _: BaseDatabaseSchemaEditor) -> None:
    '''
    Deletes all records about courses and VOS organizations.
    '''

    Course = apps.get_model(APP_NAME, 'Course')
    VOSOrganization = apps.get_model(APP_NAME, 'VOSOrganization')
    Course.objects.all().delete()
    VOSOrganization.objects.all().delete()


class Migration(BaseMigration):
    dependencies = ((APP_NAME, '0002_course_model'),)
    operations = (RunPython(insert_prepared_data, remove_prepared_data),)
