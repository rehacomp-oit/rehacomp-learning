from typing import TypeAlias

from returns.result import Result
from server.apps.core.business_error_types import FolderListFailure
from server.apps.core.value_objects import CourseFolderName


CourseFoldersListServiceResult: TypeAlias = Result[tuple[CourseFolderName, ...], FolderListFailure]
