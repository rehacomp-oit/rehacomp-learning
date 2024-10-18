from datetime import datetime
from typing import Final, final, Self

from django.core.validators import RegexValidator
from django.forms import (
    BooleanField,
    CharField,
    ChoiceField,
    EmailField,
    Form,
    IntegerField,
    Textarea,
    TypedChoiceField
)
from django.forms.widgets import Input
from django.utils.translation import gettext_lazy as _

from .domain.constants import (
    EDUCATION_INFORMATION_LENGTH,
    JOB_INFORMATION_LENGTH,
    PERSON_NAME_LENGTH,
    PHONE_NUMBER_MAX_LENGTH,
    PHONE_NUMBER_PATTERN
)


CHAR_FIELD_MIN_LENGTH: Final = 2
MIN_BIRTH_YEAR: Final = 1000
MAX_BIRTH_YEAR: Final = 3000


# Below is the definition of internal iterables for form fields with a choice
_disability_group_choices = (
    (1, _('First group based on vision'),),
    (2, _('Second group based on vision'),),
    (3, _('Third group based on vision'),),
    (4, _('Other disability'),),
    (5, _('No disability'),),
)

_training_level_choices = (
    (0, _('Zero level'),),
    (1, _('Beginner user'),),
    (2, _('Basic level'),),
    (3, _('Confident user'),),
    (4, _('Experienced user'),),
    (5, _('Advanced user'),),
)


# Definition form validatiors and widgets
_phone_number_validator = RegexValidator(
    regex=PHONE_NUMBER_PATTERN,
    message=_('The phone number does not match the specified format'),
    code='invalid_phone_number'
)

_phone_number_input = Input(
    attrs={'input_type': 'tel', 'class': 'phone-input'}
)


@final
class LearningRequestForm(Form):

    courses = ChoiceField(
        label=_('Learning course')
    )

    first_name = CharField(
        max_length=PERSON_NAME_LENGTH,
        min_length=CHAR_FIELD_MIN_LENGTH,
        label=_('First name')
    )

    patronymic = CharField(
        max_length=PERSON_NAME_LENGTH,
        min_length=CHAR_FIELD_MIN_LENGTH,
        label=_('Patronymic')
    )

    last_name = CharField(
        max_length=PERSON_NAME_LENGTH,
        min_length=CHAR_FIELD_MIN_LENGTH,
        label=_('Last name')
    )

    birth_year = IntegerField(
        max_value=MAX_BIRTH_YEAR,
        min_value=MIN_BIRTH_YEAR,
        initial=datetime.now().year,
        label=_('Birth year')
    )

    organizations = ChoiceField(
        label=_('VOS organization')
    )

    disability_group = TypedChoiceField(
        choices=_disability_group_choices,
        coerce=str,
        label=_('Disability group')
    )

    education = CharField(
        max_length=EDUCATION_INFORMATION_LENGTH,
        min_length=CHAR_FIELD_MIN_LENGTH,
        label=_('Education')
    )

    job = CharField(
        max_length=JOB_INFORMATION_LENGTH,
        min_length=CHAR_FIELD_MIN_LENGTH,
        label=_('Job information')
    )

    is_known_braille = BooleanField(
        initial=False,
        label=_('Knowledge of the Braille system')
    )

    has_device = BooleanField(
        initial=False,
        label=_('Presence of device')
    )

    training_levels = TypedChoiceField(
        choices=_training_level_choices,
        coerce=str,
        label=_('Training level')
    )

    personal_phone = CharField(
        max_length=PHONE_NUMBER_MAX_LENGTH,
        min_length=CHAR_FIELD_MIN_LENGTH,
        label=_('Personal phone number'),
        widget=Input(attrs={'input_type': 'tel'})
    )

    email = EmailField(
        label=_('Email address')
    )

    is_archived = BooleanField(
        initial=False,
        label=_('Archived')
    )

    comments = CharField(
        label=_('Note'),
        widget=Textarea(),
    )


    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['courses'].widget.attrs['autofocus'] = True


    @classmethod
    def build_unbound_form(
        cls,
        learning_course_data: tuple[tuple[int, str], ...],
        organizations_data: tuple[tuple[int, str], ...]
    ) -> Self:
        form = cls()
        form.fields['courses'].choices = learning_course_data
        form.fields['organizations'].choices = organizations_data
        return form
