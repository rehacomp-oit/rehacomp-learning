from typing import final

from django.db.migrations import CreateModel
from django.db.migrations import Migration as BaseMigration
from django.db.models import (
    BooleanField,
    CharField,
    EmailField,
    Index,
    PositiveSmallIntegerField,
)
from server.apps.request_folders.domain.enum_types import (
    DisabilityGroups,
    TrainingLevels
)
from server.common.django_tools import PKULIDField


_fields = (
    ('id', PKULIDField(auto_created=True, primary_key=True, serialize=False),),
    ('first_name', CharField(max_length=20),),
    ('patronymic', CharField(max_length=20),),
    ('last_name', CharField(max_length=20),),
    ('birth_year', PositiveSmallIntegerField(null=True),),
    ('disability_group', CharField(
        db_default=DisabilityGroups['VISION_FIRST'],
        default=DisabilityGroups['VISION_FIRST'],
        max_length=5
    ),),
    ('education_info', CharField(blank=True, db_default='', default='', max_length=80),),
    ('job_info', CharField(blank=True, db_default='', default='', max_length=80),),
    ('is_known_braille', BooleanField(db_default=False, default=False),),
    ('training_level', PositiveSmallIntegerField(db_default=TrainingLevels['ZERO'], default=TrainingLevels['ZERO']),),
    ('has_device', BooleanField(db_default=False, default=False),),
    ('personal_phone', CharField(blank=True, db_default='', default='', max_length=20),),
    ('email', EmailField(blank=True, db_default='', default='', max_length=254),)
)

_options = {
    'verbose_name': 'Person',
    'verbose_name_plural': 'Persons',
    'db_table_comment': 'Information about the candidate or student.',
    'indexes': (Index(fields=['first_name', 'patronymic', 'last_name'], name='full_name_index'),),
}


@final
class Migration(BaseMigration):
    dependencies = (('request_folders', '0002_course_model',),)
    operations = (CreateModel(name='Person', fields=_fields, options=_options),)
