from collections.abc import Callable
from typing import TypeAlias

from returns.result import Result

from ..dto import CourseDTO, RequestFormOptions
from ..results import GetCourseFoldersFailure, GetRequestFormOptionFailure


GetCourseListUsecase: TypeAlias = Callable[  # noqa: ECE001
    [],
    Result[tuple[CourseDTO, ...], GetCourseFoldersFailure]
]

GetRequestFormOptionsUsecase: TypeAlias = Callable[
    [],
    Result[RequestFormOptions, GetRequestFormOptionFailure]
]
