from typing import final

from django.db.migrations import AddField, RunSQL
from django.db.migrations import Migration as BaseMigration
from django.db.models import ForeignKey
from django.db.models.deletion import SET_NULL


_field_definition = ForeignKey(
    db_constraint=False,
    null=True,
    on_delete=SET_NULL,
    related_name='members',
    to='learning_requests.vosorganization',
    verbose_name='Related VOS organization'
)

_foreign_key_constraint_definition = (
    '-- Create constraint related_vos_fk on model person\n'
    'ALTER TABLE "learning_requests_person" ADD CONSTRAINT "related_vos_fk" '
    'FOREIGN KEY ("related_vos_organization_id") REFERENCES "learning_requests_vosorganization" ("id") '
    'ON DELETE SET NULL '
    'DEFERRABLE INITIALLY DEFERRED;'
)


@final
class Migration(BaseMigration):
    dependencies = (('learning_requests', '0003_person_model'),)

    operations = (
        AddField(model_name='person', name='related_vos_organization', field=_field_definition),
        RunSQL(_foreign_key_constraint_definition),
    )
