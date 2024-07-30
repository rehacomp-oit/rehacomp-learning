from typing import final

from django.conf import settings
from django.db.models import (
    BooleanField,
    CharField,
    CheckConstraint,
    DateTimeField,
    ForeignKey,
    Index,
    Model,
    Q,
    SET_NULL,
    TextField
)
from django.utils.translation import gettext_lazy as _
from server.utilites.common.funcs import make_ULID
from server.utilites.django_tools import PKULIDField

from .constants import LEARNING_REQUEST_STATUS_LENGTH, LearningRequestStatuses


_request_status_check = CheckConstraint(
    check=Q(status__in=LearningRequestStatuses.get_values()),
    name='status_check'
)

_created_at_index = Index(fields=('created_at',), name='created_at_index')
_updated_at_index = Index(fields=('updated_at',), name='updated_at_index')


@final
class RequestMetadata(Model):
    '''
    Meta information of learning requests.
    '''

    class Meta:
        db_table_comment = 'Meta information of learning requests.'
        verbose_name = _('Request metadata')
        verbose_name_plural = _('Request metadata')
        constraints = (_request_status_check,)
        indexes = (_created_at_index, _updated_at_index,)


    id = PKULIDField(  # noqa: VNE003
        auto_created=True,
        default=make_ULID,
        primary_key=True,
        serialize=False,
        verbose_name='id'
    )

    created_at = DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at')
    )

    updated_at = DateTimeField(
        auto_now=True,
        verbose_name=_('Updated at')
    )

    relevance = BooleanField(
        db_default=True,
        default=True,
        verbose_name=_('Relevance of  learning request')
    )

    status = CharField(
        db_comment=(
            'Available status variants for learning request: '
            '<registered>, <approved>, <rejected>, <in_archive>.'
        ),
        db_default=LearningRequestStatuses.REGISTERED,
        default=LearningRequestStatuses.REGISTERED,
        max_length=LEARNING_REQUEST_STATUS_LENGTH,
        verbose_name=_('Status of learning request')
    )

    note = TextField(
        db_default='',
        default='',
        verbose_name=_('Short text note about learning request')
    )

    course = ForeignKey(
        db_constraint=False,
        to='core.Course',
        null=True,
        on_delete=SET_NULL,
        related_name='learning_requests',
        verbose_name=_('Related course')
    )

    candidate = ForeignKey(
        db_constraint=False,
        to='core.Person',
        null=True,
        on_delete=SET_NULL,
        related_name='learning_requests',
        verbose_name=_('Related person')
    )

    author = ForeignKey(
        db_constraint=False,
        to=settings.AUTH_USER_MODEL,
        null=True,
        on_delete=SET_NULL,
        verbose_name=_('Related author')
    )


    def __str__(self) -> str:
        return str(self.created_at)
