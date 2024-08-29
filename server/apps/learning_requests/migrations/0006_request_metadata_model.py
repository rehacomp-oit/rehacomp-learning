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
    ('id', PKULIDField(
        auto_created=True,
        default=make_ULID,
        primary_key=True,
        serialize=False,
        verbose_name='id'
    )),

    ('created_at', DateTimeField(
        auto_now_add=True,
        verbose_name='Created at'
    )),

    ('updated_at', DateTimeField(
        auto_now=True,
        verbose_name='Updated at'
    )),

    ('relevance', BooleanField(
        db_default=True,
        default=True,
        verbose_name='Relevance of  learning request'
    )),

    ('status', CharField(
        db_comment=(
            'Available status variants for learning request: '
            '<registered>, <approved>, <rejected>, <in_archive>.'
        ),
        db_default=LearningRequestStatuses['REGISTERED'],
        default=LearningRequestStatuses['REGISTERED'],
        max_length=10,
        verbose_name='Status of learning request'
    )),

    ('note', TextField(
        db_default='',
        default='',
        verbose_name='Short text note about learning request'
    )),
)


_options = {
    'verbose_name': 'Request metadata',
    'verbose_name_plural': 'Request metadata',
    'db_table_comment': 'Meta information of learning requests.',
}


@final
class Migration(BaseMigration):
    dependencies = (('learning_requests', '0005_related_organization_for_person',),)
    operations = (CreateModel(name='RequestMetadata', fields=_fields, options=_options),)
