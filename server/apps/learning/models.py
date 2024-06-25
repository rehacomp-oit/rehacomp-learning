from typing import final

from django.db.models import CharField, Model, SmallAutoField
from django.utils.translation import gettext_lazy as _

from .shared_constants import VOS_ORGANIZATION_NAME_LENGTH


@final
class VOSOrganization(Model):
    '''
    All Russia Association of the Blind.
    '''

    class Meta:
        db_table = 'vos_organizations'
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
