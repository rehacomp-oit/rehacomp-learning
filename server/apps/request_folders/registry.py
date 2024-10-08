from logging import getLogger, Logger

from punq import Container

from .infrastructure.repositories import CourseFolderDjangoRepository
from .protocols.repositories import CourseFolderRepository
from .protocols.usecases import GetCourseFoldersListUseCase
from .services import GetCourseFoldersListService


# Common object for logging on all business services
_logger_object = getLogger(__name__)

folder_list_service_impl = Container()
folder_list_service_impl.register(Logger, instance=_logger_object)
folder_list_service_impl.register(CourseFolderRepository, CourseFolderDjangoRepository)
folder_list_service_impl.register(GetCourseFoldersListUseCase, GetCourseFoldersListService)
