from pathlib import Path

from django.apps.registry import Apps
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations import Migration as BaseMigration
from django.db.migrations import RunPython
from server.apps.common.services import CreateInitialDataDumpService


def _load_data(apps: Apps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    input_file = Path(__file__).parent.joinpath('initial_data.json')
    Course = apps.get_model('common', 'Course')
    VOSOrganization = apps.get_model('common', 'VOSOrganization')
    service = CreateInitialDataDumpService(Course, VOSOrganization)
    service(input_file)


class Migration(BaseMigration):

    dependencies = (('common', '0003_person_model'),)
    operations = (RunPython(_load_data),)
