from typing import final

from django.core.validators import RegexValidator
from django.db.models import (
    BooleanField,
    CASCADE,
    CharField,
    CheckConstraint,
    EmailField,
    ForeignKey,
    Model,
    PositiveSmallIntegerField,
    Q,
)

from .constants import (
    COURSE_FULL_NAME_LENGTH,
    COURSE_SHORT_NAME_LANGTH,
    DISABILITY_GROUP_LENGTH,
    DisabilityGroups,
    EDUCATION_INFORMATION_LENGTH,
    EMAIL_ADDRESS_PATTERN,
    FULL_NAME_LENGTH,
    JOB_INFORMATION_LENGTH,
    PHONE_NUMBER_MAX_LENGTH,
    PHONE_NUMBER_PATTERN,
    TrainingLevels,
    VOS_ORGANIZATION_NAME_LENGTH
)


@final
class VOSOrganization(Model):
    '''All Russia Association of the Blind'''

    class Meta:
        db_table = 'vos_organizations'
        db_table_comment = 'All Russia Association of the Blind'


    organization_name = CharField(
        max_length=VOS_ORGANIZATION_NAME_LENGTH,
        db_comment='Full name of the organization',
        unique=True,
    )


    def __str__(self) -> str:
        return self.organization_name


@final
class Course(Model):
    '''Training course conducted at the Institute'''

    class Meta:
        db_table = 'courses'
        db_table_comment = 'Training course conducted at the Institute'


    course_name = CharField(
        max_length=COURSE_FULL_NAME_LENGTH,
        db_comment='Full name of the training course',
        unique=True,
    )

    course_short_name = CharField(
        max_length=COURSE_SHORT_NAME_LANGTH,
        db_comment='Abbreviation of the course name',
        unique=True,
    )


    def __str__(self) -> str:
        return self.course_short_name


@final
class Person(Model):
    '''Information about the candidate or student'''

    class Meta:
        db_table = 'persons'
        db_table_comment = 'Information about the candidate or student'

        constraints = (
            CheckConstraint(
                check=Q(disability_group__in=DisabilityGroups.values),
                name='disability_group_variants'
            ),
            CheckConstraint(
                check=Q(training_level__lte=TrainingLevels.ADVANCED),
                name='training_level_lte_advansed',
            ),
            CheckConstraint(
                check=Q(
                    personal_phone__regex=PHONE_NUMBER_PATTERN
                ) | Q(personal_phone=''),
                name='phone_nunber_pattern',
            ),
            CheckConstraint(
                check=Q(
                    email__regex=EMAIL_ADDRESS_PATTERN
                ) | Q(email=''),
                name='email_address_pattern',
            )
        )


    first_name = CharField(max_length=FULL_NAME_LENGTH)
    patronymic = CharField(max_length=FULL_NAME_LENGTH)
    last_name = CharField(max_length=FULL_NAME_LENGTH)

    birth_year = PositiveSmallIntegerField(
        db_comment='Year of birth of the registered person',
        null=True,
    )

    disability_group = CharField(
        db_comment=(
            'Information about the visual disability group:\n'
            'v1- first group based on vision;\n'
            'v2- second group based on vision;\n'
            'v3- thurd group based on vision;\n'
            'o- other disabilities;\n'
            'n- there is no disability.'
        ),
        max_length=DISABILITY_GROUP_LENGTH,
        db_default=DisabilityGroups.VISION_FIRST,
        default=DisabilityGroups.VISION_FIRST,
    )

    education = CharField(
        blank=True,
        db_comment='Information about higher education',
        db_default='',
        default='',
        max_length=EDUCATION_INFORMATION_LENGTH,
    )

    work = CharField(
        blank=True,
        db_comment='Information about the place of work',
        db_default='',
        default='',
        max_length=JOB_INFORMATION_LENGTH,
    )

    is_known_braille = BooleanField(
        db_comment='Braille font proficiency',
        db_default=False,
        default=False,
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
    )

    has_device = BooleanField(
        db_comment='Whether a person has a smartphone or computer',
        db_default=False,
        default=False,
    )

    personal_phone = CharField(
        blank=True,
        db_comment=(
            'Personal phone number for communication. '
            'Phone number format: +7(xxx)xxx-xx-xx.'
        ),
        db_default='',
        default='',
        max_length=PHONE_NUMBER_MAX_LENGTH,
        validators=(RegexValidator(regex=PHONE_NUMBER_PATTERN),),
    )

    email = EmailField(
        blank=True,
        db_comment='Personal email address',
        db_default='',
        default='',
    )

    vos_organization = ForeignKey(
        db_comment='Related VOS organization',
        to=VOSOrganization,
        on_delete=CASCADE,
        related_name='members',
    )


    def __str__(self) -> str:
        return f'{self.first_name} {self.birth_year}'
