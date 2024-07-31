from typing import final

from django.db.migrations import CreateModel
from django.db.migrations import Migration as BaseMigration
from django.db.models.fields import CharField, SmallAutoField


_fields = (
    ('id', SmallAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )),

    ('course_name', CharField(
        max_length=256,
        unique=True,
        verbose_name='Full name of the course'
    )),

    ('course_short_name', CharField(
        max_length=10,
        unique=True,
        verbose_name='Abbreviation of the course name'
    )),
)

_options = {
    'verbose_name': 'Course',
    'verbose_name_plural': 'Courses',
    'db_table_comment': 'Training course conducted at the Institute.',
}


@final
class Migration(BaseMigration):
    dependencies = (('core', '0001_vos_organization_model'),)
    operations = (CreateModel(name='Course', fields=_fields, options=_options),)
