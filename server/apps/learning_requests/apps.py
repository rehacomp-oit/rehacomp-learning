from typing import final

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


@final
class LearningRequestsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server.apps.learning_requests'
    label = 'learning_requests'
    verbose_name = _('Learning requests')
