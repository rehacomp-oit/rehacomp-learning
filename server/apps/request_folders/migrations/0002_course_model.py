from typing import final

from django.db.migrations import CreateModel
from django.db.migrations import Migration as BaseMigration
from django.db.models.fields import CharField, SlugField
from server.common.django_tools import PKULIDField


_fields = (
    ('id', PKULIDField(auto_created=True, primary_key=True, serialize=False),),
    ('name', CharField(max_length=256, unique=True),),
    ('slug', SlugField(unique=True),),
)

_options = {
    'verbose_name': 'Course',
    'verbose_name_plural': 'Courses',
    'db_table_comment': 'Training course conducted at the Institute.',
}


@final
class Migration(BaseMigration):
    dependencies = (('request_folders', '0001_vos_organization_model'),)
    operations = (CreateModel(name='Course', fields=_fields, options=_options),)
