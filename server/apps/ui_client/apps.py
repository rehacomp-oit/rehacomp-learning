from typing import final

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


@final
class UIClientConfig(AppConfig):
    name = 'server.apps.ui_client'
    label = 'ui_client'
    verbose_name = _('Base UI client features')
