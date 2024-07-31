from typing import final

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


@final
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server.apps.core'
    label = 'core'
    verbose_name = _('core')
