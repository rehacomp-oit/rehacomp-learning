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
