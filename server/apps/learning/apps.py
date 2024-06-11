from typing import final

from django.apps import AppConfig


@final
class BaseClientFeaturesConfig(AppConfig):
    name = 'server.apps.learning'
    label = 'learning'
