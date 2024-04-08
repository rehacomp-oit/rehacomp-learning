from pathlib import Path
from typing import Final

from django.apps.registry import Apps
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations import Migration as BaseMigration
from django.db.migrations import RunPython
from server.utils import load_from_json_file


SOURCE_FILENAME: Final = 'initial_data.json'
SOURCE_FILE_PATH: Final = Path(__file__).parent.joinpath(SOURCE_FILENAME)


def add_prepared_data(apps: Apps, _: BaseDatabaseSchemaEditor) -> None:
    '''
    Adds prepared information about courses and
    VOS organizations to the database.
    '''

    source_data = load_from_json_file(SOURCE_FILE_PATH)
    Course = apps.get_model('common', 'Course')
    VOSOrganization = apps.get_model('common', 'VOSOrganization')
    Course.objects.bulk_create(
        (Course(**record) for record in source_data['courses'])
    )
    VOSOrganization.objects.bulk_create(
        (VOSOrganization(**record) for record in source_data['vos'])
    )


def clear_tables(apps: Apps, _: BaseDatabaseSchemaEditor) -> None:
    '''
    Deletes all records about courses and VOS organizations.
    '''

    Course = apps.get_model('common', 'Course')
    VOSOrganization = apps.get_model('common', 'VOSOrganization')
    Course.objects.all().delete()
    VOSOrganization.objects.all().delete()


class Migration(BaseMigration):

    dependencies = (('common', '0003_person_model'),)
    operations = (RunPython(add_prepared_data, clear_tables),)
