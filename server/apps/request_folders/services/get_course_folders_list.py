from dataclasses import dataclass
from logging import Logger
from typing import final

from returns.result import Failure, Result, Success
from server.apps.request_folders.domain.entities import CourseFolder
from server.apps.request_folders.protocols.repositories import CourseFolderRepository
from server.common.types import FailureReason


@final
@dataclass(frozen=True, slots=True)
class GetCourseFoldersListService:
    '''
    Retrieves the full list of course folders.
    '''

    repository: CourseFolderRepository
    logger: Logger


    def __call__(self) -> Result[tuple[CourseFolder, ...], FailureReason]:
        if self.repository.is_empty():
            message = 'Information about courses could not be found in the system'
            self.logger.info(message)
            return Failure(FailureReason('Empty folder list'))
        else:
            folders = self.repository.fetch_all()
            message = 'List of courses has been successfully loaded from the database'
            self.logger.info(message)
            return Success(folders)
