from typing import final

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


@final
class LearningConfig(AppConfig):
    name = 'server.apps.learning'
    label = 'learning'
    verbose_name = _('Learning')