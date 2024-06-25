from django.db.migrations import CreateModel
from django.db.migrations import Migration as BaseMigration
from django.db.models import CharField, SmallAutoField


_fields = (
    ('id', SmallAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    ('organization_name', CharField(max_length=80, unique=True, verbose_name='VOS organization name')),
)

_options = {
    'verbose_name': 'VOS organization',
    'verbose_name_plural': 'VOS organizations',
    'db_table': 'vos_organizations',
    'db_table_comment': 'All Russia Association of the Blind.',
}


class Migration(BaseMigration):

    initial = True
    dependencies = ()
    operations = (CreateModel(name='VOSOrganization', fields=_fields, options=_options),)
