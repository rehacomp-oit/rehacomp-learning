from typing import final

from django.conf import settings
from django.db.migrations import AddField, RunSQL, swappable_dependency
from django.db.migrations import Migration as BaseMigration
from django.db.models import ForeignKey
from django.db.models.deletion import SET_NULL


_fields = (
    ForeignKey(
        db_constraint=False,
        null=True,
        on_delete=SET_NULL,
        to=settings.AUTH_USER_MODEL,
        verbose_name='Request author'
    ),

    ForeignKey(
        db_constraint=False,
        null=True,
        on_delete=SET_NULL,
        related_name='learning_requests',
        to='core.person',
        verbose_name='Related person'
    ),

    ForeignKey(
        db_constraint=False,
        null=True,
        on_delete=SET_NULL,
        related_name='learning_requests',
        to='core.course',
        verbose_name='Related course'
    ),
)


# Define foreign key constraints
_author_foreign_key_definition = (
    '-- Create constraint request_author_fk on model request_metadata\n'
    'ALTER TABLE "learning_requests_requestmetadata" ADD CONSTRAINT "request_author_fk" '
    'FOREIGN KEY ("author_id") REFERENCES "auth_user" ("id") '
    'ON DELETE SET NULL '
    'DEFERRABLE INITIALLY DEFERRED;'
)

_candidate_foreign_key_definition = (
    '-- Create constraint related_person_fk on model request_metadata\n'
    'ALTER TABLE "learning_requests_requestmetadata" ADD CONSTRAINT "related_person_fk" '
    'FOREIGN KEY ("candidate_id") REFERENCES "core_person" ("id") '
    'ON DELETE SET NULL '
    'DEFERRABLE INITIALLY DEFERRED;'
)

_course_foreign_key_definition = (
    '-- Create constraint related_course on model request_metadata\n'
    'ALTER TABLE "learning_requests_requestmetadata" ADD CONSTRAINT "related_course_fk" '
    'FOREIGN KEY ("course_id") REFERENCES "core_course" ("id") '
    'ON DELETE SET NULL '
    'DEFERRABLE INITIALLY DEFERRED;'
)


@final
class Migration(BaseMigration):
    dependencies = (
        ('core', '0005_related_organization_for_person'),
        ('learning_requests', '0002_request_performance_and_checks'),
        swappable_dependency(settings.AUTH_USER_MODEL),
    )


    operations = (
        AddField(model_name='requestmetadata', name='author', field=_fields[0]),
        AddField(model_name='requestmetadata', name='candidate', field=_fields[1]),
        AddField(model_name='requestmetadata', name='course', field=_fields[2]),
        RunSQL(_author_foreign_key_definition),
        RunSQL(_candidate_foreign_key_definition),
        RunSQL(_course_foreign_key_definition),
    )
