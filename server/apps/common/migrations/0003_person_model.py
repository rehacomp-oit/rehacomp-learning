from django.core.validators import RegexValidator
from django.db.migrations import AddConstraint, CreateModel
from django.db.migrations import Migration as BaseMigration
from django.db.models import (
    BigAutoField,
    BooleanField,
    CharField,
    CheckConstraint,
    EmailField,
    ForeignKey,
    PositiveSmallIntegerField,
    Q,
)
from django.db.models.deletion import CASCADE


_fields = (
    ('id', BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID',
    ),),
    ('first_name', CharField(max_length=20)),
    ('patronymic', CharField(max_length=20)),
    ('last_name', CharField(max_length=20)),
    ('birth_year', PositiveSmallIntegerField(
        db_comment='Year of birth of the registered person',
        null=True,
    ),),
    ('disability_group', CharField(
        db_comment=(
            'Information about the visual disability group:\n'
            'v1- first group based on vision;\n'
            'v2- second group based on vision;\n'
            'v3- thurd group based on vision;\n'
            'o- other disabilities;\n'
            'n- there is no disability.'
        ),
        db_default='v1',
        default='v1',
        max_length=5,
    ),),
    ('education_info', CharField(
        blank=True,
        db_comment='Information about higher education',
        db_default='',
        default='',
        max_length=80,
    ),),
    ('job_info', CharField(
        blank=True,
        db_comment='Information about the place of work',
        db_default='',
        default='',
        max_length=80,
    ),),
    ('is_known_braille', BooleanField(
        db_comment='Braille font proficiency',
        db_default=False,
        default=False,
    ),),
    ('training_level', PositiveSmallIntegerField(
        db_comment=(
            'The level of smartphone or computer proficiency:\n'
            '0- Level zero;\n'
            '1- novice user;\n'
            '2- basic level;\n'
            '3- confident user;\n'
            '4-  experienced user;\n'
            '5- advanced user.'
        ),
        db_default=0,
        default=0,
    ),),
    ('has_device', BooleanField(
        db_comment='Whether a person has a smartphone or computer',
        db_default=False,
        default=False,
    ),),
    ('personal_phone', CharField(
        blank=True,
        db_comment=(
            'Personal phone number for communication. '
            'Phone number format: +7(xxx)xxx-xx-xx.'
        ),
        db_default='',
        default='',
        max_length=20,
        validators=(RegexValidator(
            regex='^\\+7\\(\\d{3}\\)\\d{3}\\-\\d{2}\\-\\d{2}$'
        ),)
    ),),
    ('email', EmailField(
        blank=True,
        db_comment='Personal email address',
        db_default='',
        default='',
        max_length=254,
    ),),
    ('vos_organization', ForeignKey(
        db_comment='Related VOS organization',
        on_delete=CASCADE,
        related_name='members',
        to='common.vosorganization',
    ),),
)

_options = {
    'db_table': 'persons',
    'db_table_comment': 'Information about the candidate or student',
}

# Define check constraints out the migration class for more readability
_disability_group_check = CheckConstraint(
    check=Q(('disability_group__in', ('v1', 'v2', 'v3', 'o', 'n'),)),
    name='disability_group_variants',
)

_training_level_check = CheckConstraint(
    check=Q(('training_level__lte', 5)),
    name='training_level_lte_advansed',
)

_personal_phone_check = CheckConstraint(
    check=Q(
        (
            'personal_phone__regex',
            '^\\+7\\(\\d{3}\\)\\d{3}\\-\\d{2}\\-\\d{2}$',
        ),
        ('personal_phone', '',),
        _connector='OR',
    ),
    name='phone_nunber_pattern'
)

_email_check = CheckConstraint(
    check=Q(
        ('email__regex', '^\\S+@\\S+\\.\\S+$',),
        ('email', '',),
        _connector='OR',
    ),
    name='email_address_pattern'
)


class Migration(BaseMigration):

    dependencies = (('common', '0002_course_model'),)
    operations = (
        CreateModel(name='Person', fields=_fields, options=_options,),
        AddConstraint(model_name='person', constraint=_disability_group_check),
        AddConstraint(model_name='person', constraint=_training_level_check),
        AddConstraint(model_name='person', constraint=_personal_phone_check),
        AddConstraint(model_name='person', constraint=_email_check),
    )
