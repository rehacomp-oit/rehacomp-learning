from typing import final

from django.db.migrations import CreateModel
from django.db.migrations import Migration as BaseMigration
from django.db.models import BooleanField, DateTimeField, TextField
from server.common.django_tools import PKULIDField


_fields = (
    ('id', PKULIDField(auto_created=True, primary_key=True, serialize=False),),
    ('created_at', DateTimeField(auto_now_add=True),),
    ('updated_at', DateTimeField(auto_now=True),),
    ('relevance', BooleanField(db_default=True, default=True),),
    ('note', TextField(db_default='', default=''),),
)


_options = {
    'verbose_name': 'Request metadata',
    'verbose_name_plural': 'Request metadata',
    'db_table_comment': 'Meta information of learning requests.',
}


@final
class Migration(BaseMigration):
    dependencies = (('request_folders', '0004_related_organization_for_person',),)
    operations = (CreateModel(name='RequestMetadata', fields=_fields, options=_options),)
