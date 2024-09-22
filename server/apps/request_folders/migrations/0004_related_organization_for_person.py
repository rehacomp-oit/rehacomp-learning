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
    to='request_folders.vosorganization'
)

_foreign_key_constraint_definition = (
    '-- Create constraint related_vos_fk on model person\n'
    'ALTER TABLE "request_folders_person" ADD CONSTRAINT "related_vos_fk" '
    'FOREIGN KEY ("related_vos_organization_id") REFERENCES "request_folders_vosorganization" ("id") '
    'ON DELETE SET NULL '
    'DEFERRABLE INITIALLY DEFERRED;'
)


@final
class Migration(BaseMigration):
    dependencies = (('request_folders', '0003_person_model'),)
    operations = (
        AddField(model_name='person', name='related_vos_organization', field=_field_definition),
        RunSQL(_foreign_key_constraint_definition),
    )
