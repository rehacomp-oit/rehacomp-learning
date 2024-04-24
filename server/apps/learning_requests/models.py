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

from .constants import LEARNING_REQUEST_STATUS_LENGTH, LearningRequestStatuses
from .helpers import build_upload_path


ATTACHMENT_TARGET_NAME_LENGTH: Final = 80
ATTACHMENT_PATH_LENGTH: Final = 128


@final
class LearningRequestMetadata(Model):
    '''Meta information of learning requests.'''

    class Meta:
        db_table = 'learning_requests_metadata'
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
        db_comment=(
            'Available status variants for learning requests: '
            '<registered>, <approved>, <rejected>, <in_history>'
        ),
        db_default=LearningRequestStatuses.REGISTERED,
        default=LearningRequestStatuses.REGISTERED,
        max_length=LEARNING_REQUEST_STATUS_LENGTH
    )

    candidates = ManyToManyField(
        to=Person,
        db_table='person_learning_requests',
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
        max_length=ATTACHMENT_TARGET_NAME_LENGTH
    )

    uploaded_file = FileField(
        db_comment='Фull path to the uploaded file with the original learning request.',
        unique=True,
        upload_to=build_upload_path,
        max_length=ATTACHMENT_PATH_LENGTH,
    )

    learning_request = OneToOneField(
        db_comment='Related learning request metadata.',
        to=LearningRequestMetadata,
        null=True,
        on_delete=SET_NULL
    )


    def __str__(self) -> str:
        return self.target_name
