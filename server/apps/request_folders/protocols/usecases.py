from typing import Protocol

from returns.result import Result
from server.apps.request_folders.domain.entities import CourseFolder
from server.common.types import FailureReason


class GetCourseFoldersListUseCase(Protocol):
    def __call__(self) -> Result[tuple[CourseFolder, ...], FailureReason]:
        ...
