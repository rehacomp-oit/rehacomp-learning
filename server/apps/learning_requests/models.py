from typing import final

from django.db.models import (
    BooleanField,
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    ManyToManyField,
    Model,
    TextField
)
from server.apps.common.models import Course, Person


@final
class LearningRequest(Model):

    class Meta:
        db_table = 'learning_requests'


    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    note = TextField(
        blank=True,
        db_default='',
        default='',
    )

    relevance = BooleanField(
        db_default=True,
        default=True,
    )
    status = CharField()

    candidates = ManyToManyField(
        to=Person,
        db_table='person_requests',
    )

    course = ForeignKey(
        to=Course,
        on_delete=CASCADE,
        related_name='learning_requests',
    )


    def __str__(self) -> str:
        return self.status
