from collections.abc import Callable
from typing import TypeAlias

from returns.result import Result

from ..dto import CourseFolder, RequestFormOptions
from ..results import GetCourseFoldersFailure, GetRequestFormOptionFailure


GetCourseFoldersUsecase: TypeAlias = Callable[  # noqa: ECE001
    [],
    Result[tuple[CourseFolder, ...], GetCourseFoldersFailure]
]

GetRequestFormOptionsUsecase: TypeAlias = Callable[
    [],
    Result[RequestFormOptions, GetRequestFormOptionFailure]
]
