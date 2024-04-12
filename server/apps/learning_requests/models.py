from os.path import join, splitext
from typing import Final, final

from django.db.models import (
    BooleanField,
    CharField,
    CheckConstraint,
    DateTimeField,
    FileField,
    ForeignKey,
    ManyToManyField,
    Model,
    OneToOneField,
    Q,
    SET_NULL,
    TextField
)
from server.apps.common.models import Course, Person

from .constants import (
    LEARNING_REQUEST_FILE_NAME_LENGTH,
    LEARNING_REQUEST_STATUS_LENGTH,
    LearningRequestStatuses,
)


LEARNING_REQUEST_UPLOAD_DIR: Final = 'learning_requests'


def build_path(instance: Model, source_filename: str) -> str:
    '''Returns the generated path for the uploaded learning request source file.'''

    source_file_suffix = splitext(source_filename)[1]
    new_filename = f'{instance.target_name}{source_file_suffix}'
    return join(LEARNING_REQUEST_UPLOAD_DIR, new_filename)


@final
class LearningRequest(Model):
    '''Meta information of learning requests.'''

    class Meta:
        db_table = 'learning_requests'
        db_table_comment = 'Meta information of learning requests.'

        constraints = (
            CheckConstraint(
                check=Q(status__in=LearningRequestStatuses.get_values()),
                name='status_variants'
            ),
        )


    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    note = TextField(
        blank=True,
        db_comment='A short text note about learning request.',
        db_default='',
        default='',
    )

    relevance = BooleanField(
        db_comment='Is the learning request currently relevant.',
        db_default=True,
        default=True,
    )

    status = CharField(
        db_default=LearningRequestStatuses.REGISTERED,
        default=LearningRequestStatuses.REGISTERED,
        max_length=LEARNING_REQUEST_STATUS_LENGTH
    )

    candidates = ManyToManyField(
        to=Person,
        db_table='person_requests',
    )

    course = ForeignKey(
        db_comment='Related course.',
        to=Course,
        null=True,
        on_delete=SET_NULL,
        related_name='learning_requests',
    )


    def __str__(self) -> str:
        return self.status


@final
class Attachment(Model):
    '''Defines the source file with the text of a learning request.'''

    class Meta:
        db_table = 'attachments'
        db_table_comment = 'Defines the source file with the text of a learning request.'


    target_name = CharField(
        db_comment='File name without extention.',
        primary_key=True,
        max_length=LEARNING_REQUEST_FILE_NAME_LENGTH
    )

    uploaded_file = FileField(
        upload_to=build_path,
    )

    learning_request = OneToOneField(
        db_comment='Related learning request metadata.',
        to=LearningRequest,
        null=True,
        on_delete=SET_NULL
    )


    def __str__(self) -> str:
        return self.target_name
