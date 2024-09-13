from typing import Protocol, TypeAlias

from returns.result import Result
from server.apps.learning_requests.domain.value_objects import CourseFolderName
from server.common.types import FailureReason


CourseFoldersListResult: TypeAlias = Result[tuple[CourseFolderName, ...], FailureReason]


class ShowCourseFoldersListUseCase(Protocol):
    def __call__(self) -> CourseFoldersListResult:
        ...
