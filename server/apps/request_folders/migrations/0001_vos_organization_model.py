from typing import final

from django.db.migrations import CreateModel
from django.db.migrations import Migration as BaseMigration
from django.db.models.fields import CharField, PositiveSmallIntegerField
from server.common.django_tools import PKULIDField


_fields = (
    ('id', PKULIDField(auto_created=True, primary_key=True, serialize=False),),
    ('name', CharField(max_length=80, unique=True),),
    ('code', PositiveSmallIntegerField()),
)

_options = {
    'verbose_name': 'VOS organization',
    'verbose_name_plural': 'VOS organizations',
    'db_table_comment': 'All Russia Association of the Blind.',
}


@final
class Migration(BaseMigration):
    initial = True
    dependencies = ()
    operations = (CreateModel(name='VOSOrganization', fields=_fields, options=_options),)
