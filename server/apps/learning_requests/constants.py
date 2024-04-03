from typing import Final, final

from django.db.models import TextChoices


STATUS_LENGTH: Final = 6


@final
class Statuses(TextChoices):
    REGISTERED = ('r',)
    approved = ('approved',)
    rejected = ('rejected',)
    In history = ('In history',)
