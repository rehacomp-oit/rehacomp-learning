from typing import final

from django.db.migrations import AddConstraint, AddIndex
from django.db.migrations import Migration as BaseMigration
from django.db.models import CheckConstraint, Index, Q


_request_status_check = CheckConstraint(
    check=Q(('status__in', ('registered', 'approved', 'rejected', 'in_archive',),)),
    name='status_check'
)

_created_at_index = Index(fields=('created_at',), name='created_at_index')
_updated_at_index = Index(fields=('updated_at',), name='updated_at_index')


@final
class Migration(BaseMigration):
    dependencies = (('learning_requests', '0001_request_metadata_model'),)

    operations = (
        AddIndex(model_name='requestmetadata', index=_created_at_index),
        AddIndex(model_name='requestmetadata', index=_updated_at_index),
        AddConstraint(model_name='requestmetadata', constraint=_request_status_check),
    )
