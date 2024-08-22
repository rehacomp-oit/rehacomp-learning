from typing import Protocol

from .results import CourseFoldersListServiceResult


class CourseFoldersListUseCase(Protocol):
    def __call__(self) -> CourseFoldersListServiceResult:
        ...
