from typing import final, override

from django.apps import AppConfig
from django.conf import settings


@final
class CoreConfig(AppConfig):
    name = 'server.core'


    @override
    def ready(self) -> None:
        from .di import initialize_di_container
        modules = getattr(settings, 'DI_BOOTSTRAP_MODULES', ())
        initialize_di_container(modules)
