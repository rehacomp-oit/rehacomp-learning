from typing import final

from django.db.migrations import AddIndex
from django.db.migrations import Migration as BaseMigration
from django.db.models import Index


_created_at_index = Index(fields=('created_at',), name='created_at_index')
_updated_at_index = Index(fields=('updated_at',), name='updated_at_index')


@final
class Migration(BaseMigration):
    dependencies = (('request_folders', '0005_request_metadata_model'),)
    operations = (
        AddIndex(model_name='requestmetadata', index=_created_at_index),
        AddIndex(model_name='requestmetadata', index=_updated_at_index),
    )
