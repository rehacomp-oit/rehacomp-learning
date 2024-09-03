from typing import final

from django.db.migrations import CreateModel
from django.db.migrations import Migration as BaseMigration
from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
    TextField
)
from server.apps.learning_requests.domain.enum_types import LearningRequestStatuses
from server.common.django_tools import PKULIDField
from server.common.utils import make_ULID


_fields = (
    ('id', PKULIDField(auto_created=True, default=make_ULID, primary_key=True, serialize=False),),
    ('created_at', DateTimeField(auto_now_add=True),),
    ('updated_at', DateTimeField(auto_now=True),),
    ('relevance', BooleanField(db_default=True, default=True),),
    ('status', CharField(
        db_default=LearningRequestStatuses['REGISTERED'],
        default=LearningRequestStatuses['REGISTERED'],
        max_length=10
    ),),
    ('note', TextField(db_default='', default=''),),
)


_options = {
    'verbose_name': 'Request metadata',
    'verbose_name_plural': 'Request metadata',
    'db_table_comment': 'Meta information of learning requests.',
}


@final
class Migration(BaseMigration):
    dependencies = (('learning_requests', '0004_related_organization_for_person',),)
    operations = (CreateModel(name='RequestMetadata', fields=_fields, options=_options),)
