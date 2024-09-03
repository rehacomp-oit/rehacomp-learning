from typing import final

from django.conf import settings
from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
    EmailField,
    ForeignKey,
    Index,
    Model,
    PositiveSmallIntegerField,
    SET_NULL,
    SlugField,
    TextField
)
from django.db.models.fields import SmallAutoField
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from server.common.django_tools import PKULIDField
from server.common.utils import make_ULID, transliterate_text

from .domain.constants import (
    COURSE_FULL_NAME_LENGTH,
    COURSE_SHORT_NAME_LANGTH,
    DISABILITY_GROUP_LENGTH,
    EDUCATION_INFORMATION_LENGTH,
    JOB_INFORMATION_LENGTH,
    LEARNING_REQUEST_STATUS_LENGTH,
    PERSON_NAME_LENGTH,
    PHONE_NUMBER_MAX_LENGTH,
    VOS_ORGANIZATION_NAME_LENGTH
)
from .domain.enum_types import DisabilityGroups, LearningRequestStatuses, TrainingLevels


_created_at_index = Index(fields=('created_at',), name='created_at_index')
_updated_at_index = Index(fields=('updated_at',), name='updated_at_index')


@final
class VOSOrganization(Model):
    '''
    All Russia Association of the Blind.
    '''

    class Meta:
        db_table_comment = 'All Russia Association of the Blind.'
        verbose_name = _('VOS organization')
        verbose_name_plural = _('VOS organizations')


    id = SmallAutoField(auto_created=True, primary_key=True,)  # noqa: VNE003
    organization_name = CharField(max_length=VOS_ORGANIZATION_NAME_LENGTH, unique=True)


    def __str__(self) -> str:
        return self.organization_name


@final
class Course(Model):
    '''
    Training course conducted at the Institute.
    '''

    class Meta:
        db_table_comment = 'Training course conducted at the Institute.'
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')


    id = SmallAutoField(auto_created=True, primary_key=True)  # noqa: VNE003
    name = CharField(max_length=COURSE_FULL_NAME_LENGTH, unique=True)
    slug = SlugField(unique=True)
    short_name = CharField(max_length=COURSE_SHORT_NAME_LANGTH, unique=True)


    def __str__(self) -> str:
        return self.short_name


    def save(self, *args, **kwargs) -> None:
        if not self.id and not self.slug:
            self.slug = slugify(transliterate_text(self.name))

        super().save(*args, **kwargs)


@final
class Person(Model):
    '''
    Information about the candidate or student.
    '''

    class Meta:
        db_table_comment = 'Information about the candidate or student.'
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')
        indexes = (
            Index(('first_name', 'patronymic', 'last_name',), name='full_name_index'),
        )


    first_name = CharField(max_length=PERSON_NAME_LENGTH)
    patronymic = CharField(max_length=PERSON_NAME_LENGTH)
    last_name = CharField(max_length=PERSON_NAME_LENGTH)
    birth_year = PositiveSmallIntegerField(null=True)
    disability_group = CharField(
        max_length=DISABILITY_GROUP_LENGTH,
        db_default=DisabilityGroups.VISION_FIRST,
        default=DisabilityGroups.VISION_FIRST
    )
    education_info = CharField(
        blank=True,
        db_default='',
        default='',
        max_length=EDUCATION_INFORMATION_LENGTH
    )
    job_info = CharField(
        blank=True,
        db_default='',
        default='',
        max_length=JOB_INFORMATION_LENGTH
    )
    is_known_braille = BooleanField(db_default=False, default=False)
    training_level = PositiveSmallIntegerField(db_default=TrainingLevels.ZERO, default=TrainingLevels.ZERO)
    has_device = BooleanField(db_default=False, default=False)
    personal_phone = CharField(
        blank=True,
        db_default='',
        default='',
        max_length=PHONE_NUMBER_MAX_LENGTH
    )
    email = EmailField(
        blank=True,
        db_default='',
        default='',
    )

    # Database level constraint will be defined in migration using raw sql
    related_vos_organization = ForeignKey(
        db_constraint=False,
        null=True,
        to=VOSOrganization,
        on_delete=SET_NULL,
        related_name='members'
    )


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


@final
class RequestMetadata(Model):
    '''
    Meta information of learning requests.
    '''

    class Meta:
        db_table_comment = 'Meta information of learning requests.'
        verbose_name = _('Request metadata')
        verbose_name_plural = _('Request metadata')
        indexes = (_created_at_index, _updated_at_index,)


    id = PKULIDField(auto_created=True, default=make_ULID, primary_key=True)  # noqa: VNE003
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    relevance = BooleanField(db_default=True, default=True)
    status = CharField(
        db_default=LearningRequestStatuses.REGISTERED,
        default=LearningRequestStatuses.REGISTERED,
        max_length=LEARNING_REQUEST_STATUS_LENGTH
    )
    note = TextField(db_default='', default='')

    course = ForeignKey(
        db_constraint=False,
        to='Course',
        null=True,
        on_delete=SET_NULL,
        related_name='learning_requests'
    )
    candidate = ForeignKey(
        db_constraint=False,
        to='Person',
        null=True,
        on_delete=SET_NULL,
        related_name='learning_requests'
    )
    author = ForeignKey(
        db_constraint=False,
        to=settings.AUTH_USER_MODEL,
        null=True,
        on_delete=SET_NULL
    )


    def __str__(self) -> str:
        return str(self.created_at)
