from typing import final

from django.apps import AppConfig


@final
class LearningRequestsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'learning_requests'
