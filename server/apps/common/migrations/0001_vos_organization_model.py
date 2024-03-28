from django.db.migrations import CreateModel
from django.db.migrations import Migration as BaseMigration
from django.db.models import BigAutoField, CharField


_fields = (
    ('id', BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID',
    )),
    ('organization_name', CharField(
        db_comment='Full name of the organization',
        max_length=80,
        unique=True,
    )),
)

_options = {
    'db_table': 'vos_organizations',
    'db_table_comment': 'All Russia Association of the Blind',
}


class Migration(BaseMigration):

    initial = True
    dependencies = ()
    operations = (
        CreateModel(name='VOSOrganization', fields=_fields, options=_options,),
    )
