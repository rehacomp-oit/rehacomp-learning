from abc import ABC, abstractmethod
from typing import Any

from django.db.models import Model
from server.common.types import BaseEntity


class BaseRepository(ABC):
    _model: Model


    def fetch_all(self) -> Iterable[BaseEntity]:
        queryset = self._model.objects.values_list()
        return tuple(self._to_entity(raw) for raw in queryset.iterator())


    def fetch_by_id(self, entity_id: Any) -> BaseEntity:
        queryset = self._model.objects.values_list()
        return self._to_entity(queryset.get(id=entity_id))


    def is_empty(self) -> bool:
        return self._model.objects.exists()


    @abstractmethod
    def _to_entity(self, raw_data: tuple[Any, ...]) -> BaseEntity:
        return NotImplemented
