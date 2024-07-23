from typing import final

from django.db.models import (
    BooleanField,
    CharField,
    CheckConstraint,
    EmailField,
    ForeignKey,
    Index,
    Model,
    PositiveSmallIntegerField,
    Q,
    SET_NULL
)
from django.db.models.fields import SmallAutoField
from django.utils.translation import gettext_lazy as _
from server.utilites.django_tools import PKULIDField
from ulid import new as new_ulid

from .shared_constants import (
    COURSE_FULL_NAME_LENGTH,
    COURSE_SHORT_NAME_LANGTH,
    DISABILITY_GROUP_LENGTH,
    DisabilityGroups,
    EDUCATION_INFORMATION_LENGTH,
    EMAIL_ADDRESS_PATTERN,
    JOB_INFORMATION_LENGTH,
    PERSON_NAME_LENGTH,
    PHONE_NUMBER_MAX_LENGTH,
    TrainingLevels,
    VOS_ORGANIZATION_NAME_LENGTH
)


_disability_group_check = CheckConstraint(
    check=Q(disability_group__in=DisabilityGroups.get_values()),
    name='disability_group_check'
)

_phone_nunber_check = CheckConstraint(
    check=Q(personal_phone__regex=r'^\d+$') | Q(personal_phone=''),
    name='phone_nunber_check'
)

_email_pattern_check = CheckConstraint(
    check=Q(email__regex=EMAIL_ADDRESS_PATTERN) | Q(email=''),
    name='email_pattern_check',
)

_person_full_name_index = Index(
    fields=('first_name', 'patronymic', 'last_name',),
    name='full_name_index'
)


@final
class VOSOrganization(Model):
    '''
    All Russia Association of the Blind.
    '''

    class Meta:
        db_table_comment = 'All Russia Association of the Blind.'
        verbose_name = _('VOS organization')
        verbose_name_plural = _('VOS organizations')


    id = SmallAutoField(  # noqa: VNE003
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )

    organization_name = CharField(
        max_length=VOS_ORGANIZATION_NAME_LENGTH,
        unique=True,
        verbose_name=_('VOS organization name')
    )


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


    id = SmallAutoField(  # noqa: VNE003
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )

    course_name = CharField(
        max_length=COURSE_FULL_NAME_LENGTH,
        unique=True,
        verbose_name=_('Full name of the course')
    )

    course_short_name = CharField(
        max_length=COURSE_SHORT_NAME_LANGTH,
        unique=True,
        verbose_name=_('Abbreviation of the course name')
    )


    def __str__(self) -> str:
        return self.course_short_name


@final
class Person(Model):
    '''
    Information about the candidate or student.
    '''

    class Meta:
        db_table_comment = 'Information about the candidate or student.'
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')
        constraints = (_disability_group_check, _phone_nunber_check, _email_pattern_check,)
        indexes = (_person_full_name_index,)


    id = PKULIDField(  # noqa: VNE003
        auto_created=True,
        default=new_ulid,
        primary_key=True,
        serialize=False,
        verbose_name='id'
    )

    first_name = CharField(
        max_length=PERSON_NAME_LENGTH,
        verbose_name=_('First name')
    )

    patronymic = CharField(
        max_length=PERSON_NAME_LENGTH,
        verbose_name=_('Patronymic')
    )

    last_name = CharField(
        max_length=PERSON_NAME_LENGTH,
        verbose_name=_('Last name')
    )

    birth_year = PositiveSmallIntegerField(
        null=True,
        verbose_name=_('Person\'s birth year')
    )

    disability_group = CharField(
        db_comment=(
            'Information about the visual disability group:\n'
            'v1- first group based on vision;\n'
            'v2- second group based on vision;\n'
            'v3- thurd group based on vision;\n'
            'o- other disabilities;\n'
            'n- no disability.'
        ),
        max_length=DISABILITY_GROUP_LENGTH,
        db_default=DisabilityGroups.VISION_FIRST,
        default=DisabilityGroups.VISION_FIRST,
        verbose_name=_('Disability group')
    )

    education_info = CharField(
        blank=True,
        db_default='',
        default='',
        max_length=EDUCATION_INFORMATION_LENGTH,
        verbose_name=_('Education')
    )

    job_info = CharField(
        blank=True,
        db_default='',
        default='',
        max_length=JOB_INFORMATION_LENGTH,
        verbose_name=_('Person\'s job')
    )

    is_known_braille = BooleanField(
        db_default=False,
        default=False,
        verbose_name=_('Braille font proficiency')
    )

    training_level = PositiveSmallIntegerField(
        db_comment=(
            'The level of smartphone or computer proficiency:\n'
            '0- Level zero;\n'
            '1- novice user;\n'
            '2- basic level;\n'
            '3- confident user;\n'
            '4-  experienced user;\n'
            '5- advanced user.'
        ),
        db_default=TrainingLevels.ZERO,
        default=TrainingLevels.ZERO,
        verbose_name=_('Training Level')
    )

    has_device = BooleanField(
        db_default=False,
        default=False,
        verbose_name=_('Has device')
    )

    personal_phone = CharField(
        blank=True,
        db_default='',
        default='',
        max_length=PHONE_NUMBER_MAX_LENGTH,
        verbose_name=_('Personal phone number')
    )

    email = EmailField(
        blank=True,
        db_default='',
        default='',
        verbose_name=_('Personal email address')
    )

    # constraint in migration
    related_vos_organization = ForeignKey(
        db_constraint=False,
        null=True,
        to=VOSOrganization,
        on_delete=SET_NULL,
        related_name='members',
        verbose_name=_('Related VOS organization')
    )


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
