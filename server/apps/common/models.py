from typing import final

from django.db.models import CharField, Model


@final
class VOSOrganization(Model):
    '''All Russia Association of the Blind'''

    class Meta:
        db_table = 'vos_organizations'
        db_table_comment = 'All Russia Association of the Blind'
        verbose_name = 'организация ВОС'
        verbose_name_plural = 'организации ВОС'


    organization_name = CharField(
        max_length=80,
        db_comment='Full name of the organization',
        verbose_name='Наиминование организации ВОС',
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
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


    course_name = CharField(
        max_length=80,
        db_comment='Full name of the training course',
        verbose_name='Полное название курса',
        unique=True,
    )

    course_short_name = CharField(
        max_length=10,
        db_comment='Abbreviation of the course name',
        verbose_name='Аббревиатура названия курса',
        unique=True,
    )


    def __str__(self) -> str:
        return self.course_short_name
