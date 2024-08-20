from typing import final

from django.db.migrations import CreateModel
from django.db.migrations import Migration as BaseMigration
from django.db.models import (
    BigAutoField,
    BooleanField,
    CharField,
    EmailField,
    Index,
    PositiveSmallIntegerField,
)
from server.apps.core.domain.enum_types import (
    DisabilityGroups,
    TrainingLevels
)


_fields = (
    ('id', BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )),

    ('first_name', CharField(
        max_length=20,
        verbose_name='First name'
    )),

    ('patronymic', CharField(
        max_length=20,
        verbose_name='Patronymic'
    )),

    ('last_name', CharField(
        max_length=20,
        verbose_name='Last name'
    )),

    ('birth_year', PositiveSmallIntegerField(
        null=True,
        verbose_name='Person\'s birth year'
    )),

    ('disability_group', CharField(
        db_comment=(
            'Information about the visual disability group:\n'
            'v1- first group based on vision;\n'
            'v2- second group based on vision;\n'
            'v3- thurd group based on vision;\n'
            'o- other disabilities;\n'
            'n- no disability.'
        ),
        db_default=DisabilityGroups['VISION_FIRST'],
        default=DisabilityGroups['VISION_FIRST'],
        max_length=5,
        verbose_name='Disability group'
    )),

    ('education_info', CharField(
        blank=True,
        db_default='',
        default='',
        max_length=80,
        verbose_name='Education'
    )),

    ('job_info', CharField(
        blank=True,
        db_default='',
        default='',
        max_length=80,
        verbose_name='Person\'s job'
    )),

    ('is_known_braille', BooleanField(
        db_default=False,
        default=False,
        verbose_name='Braille font proficiency'
    )),

    ('training_level', PositiveSmallIntegerField(
        db_comment=(
            'The level of smartphone or computer proficiency:\n'
            '0- Level zero;\n'
            '1- novice user;\n'
            '2- basic level;\n'
            '3- confident user;\n'
            '4- experienced user;\n'
            '5- advanced user.'
        ),
        db_default=TrainingLevels['ZERO'],
        default=TrainingLevels['ZERO'],
        verbose_name='Training Level'
    )),

    ('has_device', BooleanField(
        db_default=False,
        default=False,
        verbose_name='Has device'
    )),

    ('personal_phone', CharField(
        blank=True,
        db_default='',
        default='',
        max_length=20,
        verbose_name='Personal phone number'
    )),

    ('email', EmailField(
        blank=True,
        db_default='',
        default='',
        max_length=254,
        verbose_name='Personal email address'
    )),
)

_options = {
    'verbose_name': 'Person',
    'verbose_name_plural': 'Persons',
    'db_table_comment': 'Information about the candidate or student.',
    'indexes': (Index(fields=['first_name', 'patronymic', 'last_name'], name='full_name_index'),),
}


@final
class Migration(BaseMigration):
    dependencies = (('core', '0002_course_model',),)
    operations = (CreateModel(name='Person', fields=_fields, options=_options),)
