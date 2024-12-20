from typing import Any, Protocol

from ..enum_types import DisabilityGroup, TrainingLevel


class Translator(Protocol):
    def get_all_translations(self) -> tuple[tuple[Any, str], ...]:
        ...


class TrainingLevelTranslator(Translator, Protocol):
    def translate(self, level: TrainingLevel) -> str:
        ...


class DisabilityGroupTranslator(Translator, Protocol):
    def translate(self, group: DisabilityGroup) -> str:
        ...
