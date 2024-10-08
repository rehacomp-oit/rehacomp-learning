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
        to='learning_requests.person',
        verbose_name='Related person'
    ),

    ForeignKey(
        db_constraint=False,
        null=True,
        on_delete=SET_NULL,
        related_name='learning_requests',
        to='learning_requests.course',
        verbose_name='Related course'
    ),
)


# Define foreign key constraints
_candidate_foreign_key_definition = (
    '-- Create constraint related_person_fk on model request_metadata\n'
    'ALTER TABLE "learning_requests_requestmetadata" ADD CONSTRAINT "related_person_fk" '
    'FOREIGN KEY ("candidate_id") REFERENCES "learning_requests_person" ("id") '
    'ON DELETE SET NULL '
    'DEFERRABLE INITIALLY DEFERRED;'
)

_course_foreign_key_definition = (
    '-- Create constraint related_course on model request_metadata\n'
    'ALTER TABLE "learning_requests_requestmetadata" ADD CONSTRAINT "related_course_fk" '
    'FOREIGN KEY ("course_id") REFERENCES "learning_requests_course" ("id") '
    'ON DELETE SET NULL '
    'DEFERRABLE INITIALLY DEFERRED;'
)


@final
class Migration(BaseMigration):
    dependencies = (
        ('learning_requests', '0004_related_organization_for_person'),
        ('learning_requests', '0006_request_metadata_performance'),
    )


    operations = (
        AddField(model_name='requestmetadata', name='candidate', field=_fields[0]),
        AddField(model_name='requestmetadata', name='course', field=_fields[1]),
        RunSQL(_candidate_foreign_key_definition),
        RunSQL(_course_foreign_key_definition),
    )
