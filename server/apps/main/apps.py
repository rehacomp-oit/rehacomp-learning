from typing import final

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


@final
class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server.apps.main'
    label = 'main'
    verbose_name = _('Main')
