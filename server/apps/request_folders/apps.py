from typing import final

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


@final
class RequestFoldersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server.apps.request_folders'
    label = 'request_folders'
    verbose_name = _('Request folders')
