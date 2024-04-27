from typing import final

from django.apps import AppConfig


@final
class BaseClientFeaturesConfig(AppConfig):
    name = 'server.apps.base_client_features'
    label = 'base_client_features'
