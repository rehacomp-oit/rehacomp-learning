'''
This module implements translator objects for the application infrastructure layer,
specifically designed to translate domain-specific objects into another language.
These translations are utilized in views for the localized display of information.
'''

from typing import final

from django.utils.translation import gettext_lazy as _

from ..domain.enum_types import DisabilityGroup, TrainingLevel


@final
class TrainingLevelDjangoTranslator:
    __slots__ = ('__translation_table', '__default',)


    def __init__(self) -> None:
        self.__default = _('unknown')
        self.__translation_table = {
            TrainingLevel.ZERO: _('Zero level'),
            TrainingLevel.BEGINNER: _('Beginner user'),
            TrainingLevel.BASIC: _('Basic level'),
            TrainingLevel.CONFIDENT: _('Confident user'),
            TrainingLevel.EXPERIENCED: _('Experienced user'),
            TrainingLevel.ADVANCED: _('Advanced user'),
        }


    def translate(self, level: TrainingLevel) -> str:
        return self.__translation_table.get(level, self.__default)


    def get_all_translations(self) -> tuple[tuple[int, str], ...]:
        items = ((value.value, msg) for value, msg in self.__translation_table.items())
        return tuple(items)


@final
class DisabilityGroupDjangoTranslator:
    __slots__ = ('__translation_table', '__default',)


    def __init__(self) -> None:
        self.__default = _('unknown')
        self.__translation_table = {
            DisabilityGroup.VISION_FIRST: _('First group based on vision'),
            DisabilityGroup.VISION_SECOND: _('Second group based on vision'),
            DisabilityGroup.VISION_THURD: _('Third group based on vision'),
            DisabilityGroup.OTHER: _('Other disability'),
            DisabilityGroup.NOTHING: _('No disability'),
        }


    def translate(self, group: DisabilityGroup) -> str:
        return self.__translation_table.get(group, self.__default)


    def get_all_translations(self) -> tuple[tuple[int, str], ...]:
        items = ((value.value, msg) for value, msg in self.__translation_table.items())
        return tuple(items)
