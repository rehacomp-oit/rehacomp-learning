from dataclasses import dataclass
from typing import final

from returns.result import Failure, Result, Success

from .business_error_types import FolderListFailure
from .interfaces.repositories import CourseRepository
from .value_objects import CourseFolderName


@final
@dataclass(frozen=True, slots=True)
class CourseFoldersListService:
    repository: CourseRepository


    def __call__(self) -> Result[tuple[CourseFolderName, ...], FolderListFailure]:
        return self._load_course_names()\
            .bind(self._Check_for_emptiness)\
            .bind(self._make_folders_list)


    def _load_course_names(self) -> Success[tuple[str, ...]]:
        return Success(self.repository.load_course_full_names())


    def _Check_for_emptiness(self, course_names: tuple[str, ...]) -> Result[tuple[str, ...], FolderListFailure]:
        if not course_names:
            return Failure(FolderListFailure.EMPTY_LIST)
        else:
            return Success(course_names)


    def _make_folders_list(
        self,
        course_names: tuple[str, ...]
    ) -> Result[tuple[CourseFolderName, ...], FolderListFailure]:
        try:
            folders = tuple(CourseFolderName(name) for name in course_names)
        except ValueError:
            return Failure(FolderListFailure.BROKEN_FOLDER_NAME)
        else:
            return Success(folders)
