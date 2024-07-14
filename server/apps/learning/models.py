from typing import final

from django.db.models import Model
from django.db.models.fields import CharField, SmallAutoField
from django.utils.translation import gettext_lazy as _

from .shared_constants import COURSE_FULL_NAME_LENGTH, COURSE_SHORT_NAME_LANGTH, VOS_ORGANIZATION_NAME_LENGTH


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
