from typing import final

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


@final
class AccountsConfig(AppConfig):
    name = 'server.apps.accounts'
    label = 'accounts'
    verbose_name = _('Accounts')
