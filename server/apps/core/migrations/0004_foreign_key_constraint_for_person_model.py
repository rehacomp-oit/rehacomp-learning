from django.db.migrations import Migration as BaseMigration
from django.db.migrations import RunSQL


# Define foreign key constraint by raw sql
_constraint_definition = (
    '-- Create constraint related_vos_fk on model person\n'
    'ALTER TABLE "core_person" '
    'ADD CONSTRAINT "related_vos_fk" '
    'FOREIGN KEY ("related_vos_organization_id") REFERENCES "core_vosorganization" ("id") '
    'ON DELETE SET NULL '
    'DEFERRABLE INITIALLY DEFERRED;'
)


class Migration(BaseMigration):
    dependencies = (('core', '0003_person_model'),)
    operations = (RunSQL(_constraint_definition),)
