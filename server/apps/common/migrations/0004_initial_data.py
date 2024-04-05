from pathlib import Path
from typing import Final

from django.apps.registry import Apps
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations import Migration as BaseMigration
from django.db.migrations import RunPython
from server.utils import load_from_json_file


FILENAME: Final = 'initial_data.json'

source_data = load_from_json_file(Path(__file__).parent.joinpath(FILENAME))


def load_data(apps: Apps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    Course = apps.get_model('common', 'Course')
    VOSOrganization = apps.get_model('common', 'VOSOrganization')
    Course.objects.bulk_create(
        (Course(**record) for record in source_data['courses'])
    )
    VOSOrganization.objects.bulk_create(
        (VOSOrganization(**record) for record in source_data['vos'])
    )


def remove_data(apps: Apps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    Course = apps.get_model('common', 'Course')
    VOSOrganization = apps.get_model('common', 'VOSOrganization')

    for record in source_data['courses']:
        Course.objects.filter(
            course_short_name=record['course_short_name']
        ).delete()

    for record in source_data['vos']:
        VOSOrganization.objects.filter(
            organization_name=record['organization_name']
        ).delete()


class Migration(BaseMigration):

    dependencies = (('common', '0003_person_model'),)
    operations = (RunPython(load_data, remove_data),)
