from dataclasses import dataclass
from logging import Logger
from typing import final

from returns.io import IOResult
from returns.result import Failure, Result, Success
from server.apps.request_folders.domain.results import GetRequestFormOptionFailure
from server.apps.request_folders.domain.value_objects import RequestFormOptions
from server.apps.request_folders.protocols.repositories import RequestFormOptionsRepository


@final
@dataclass(frozen=True, slots=True)
class GetRequestFormOptionsService:
    logger: Logger
    repository: RequestFormOptionsRepository


    def __call__(self) -> IOResult[RequestFormOptions, GetRequestFormOptionFailure]:
        return self.repository.fetch()\
            .alt(self._handle_infrastructure_error)\
            .bind_result(self._process_selected_data)


    def _handle_infrastructure_error(self, exception_object: Exception) -> GetRequestFormOptionFailure:
        return GetRequestFormOptionFailure.CRITICAL_FAILURE


    def _process_selected_data(
        self,
        data: RequestFormOptions | None
    ) -> Result[RequestFormOptions, GetRequestFormOptionFailure]:
        if not data:
            return Failure(GetRequestFormOptionFailure.MISSING_DATA)
        else:
            return Success(data)
