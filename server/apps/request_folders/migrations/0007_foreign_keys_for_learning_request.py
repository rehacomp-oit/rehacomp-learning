from typing import final

from django.db.migrations import AddField, RunSQL
from django.db.migrations import Migration as BaseMigration
from django.db.models import ForeignKey
from django.db.models.deletion import SET_NULL


_fields = (
    ForeignKey(
        db_constraint=False,
        null=True,
        on_delete=SET_NULL,
        related_name='learning_requests',
        to='request_folders.person',
        verbose_name='Related person'
    ),

    ForeignKey(
        db_constraint=False,
        null=True,
        on_delete=SET_NULL,
        related_name='learning_requests',
        to='request_folders.course',
        verbose_name='Related course'
    ),
)


# Define foreign key constraints
_candidate_foreign_key_definition = (
    '-- Create constraint related_person_fk on model request_metadata\n'
    'ALTER TABLE "request_folders_requestmetadata" ADD CONSTRAINT "related_person_fk" '
    'FOREIGN KEY ("candidate_id") REFERENCES "request_folders_person" ("id") '
    'ON DELETE SET NULL '
    'DEFERRABLE INITIALLY DEFERRED;'
)

_course_foreign_key_definition = (
    '-- Create constraint related_course on model request_metadata\n'
    'ALTER TABLE "request_folders_requestmetadata" ADD CONSTRAINT "related_course_fk" '
    'FOREIGN KEY ("course_id") REFERENCES "request_folders_course" ("id") '
    'ON DELETE SET NULL '
    'DEFERRABLE INITIALLY DEFERRED;'
)


@final
class Migration(BaseMigration):
    dependencies = (
        ('request_folders', '0004_related_organization_for_person'),
        ('request_folders', '0006_request_metadata_performance'),
    )

    operations = (
        AddField(model_name='requestmetadata', name='candidate', field=_fields[0]),
        AddField(model_name='requestmetadata', name='course', field=_fields[1]),
        RunSQL(_candidate_foreign_key_definition),
        RunSQL(_course_foreign_key_definition),
    )
