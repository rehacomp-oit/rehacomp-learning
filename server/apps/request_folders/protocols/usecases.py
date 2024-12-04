from collections.abc import Callable
from typing import TypeAlias

from returns.io import IOResult
from server.apps.request_folders.domain.results import GetCourseFoldersFailure, GetRequestFormOptionFailure
from server.apps.request_folders.domain.value_objects import CourseFolder, RequestFormOptions


GetCourseFoldersUsecase: TypeAlias = Callable[  # noqa: ECE001
    [],
    IOResult[tuple[CourseFolder, ...], GetCourseFoldersFailure]
]

GetRequestFormOptionsUsecase: TypeAlias = Callable[
    [],
    IOResult[RequestFormOptions, GetRequestFormOptionFailure]
]
