from logging import getLogger, Logger

from punq import Container
from server.common.protocols import HttpController

from .infrastructure.repositories import CourseFolderDjangoRepository, RequestFormOptionsDjangoRepository
from .protocols.repositories import CourseFolderRepository, RequestFormOptionsRepository
from .protocols.usecases import GetCourseFoldersUsecase, GetRequestFormOptionsUsecase
from .services import GetCourseFoldersService, GetRequestFormOptionsService
from .views import AddLearningRequestView, GetFoldersListView


# Common object for logging on all business services
_logger_object = getLogger(__name__)

folder_list_service_impl = Container()
folder_list_service_impl.register(Logger, instance=_logger_object)
folder_list_service_impl.register(CourseFolderRepository, CourseFolderDjangoRepository)
folder_list_service_impl.register(GetCourseFoldersUsecase, GetCourseFoldersService)
folder_list_service_impl.register(HttpController, GetFoldersListView)

add_learning_request_impl = Container()
add_learning_request_impl.register(Logger, instance=_logger_object)
add_learning_request_impl.register(RequestFormOptionsRepository, RequestFormOptionsDjangoRepository)
add_learning_request_impl.register(GetRequestFormOptionsUsecase, GetRequestFormOptionsService)
add_learning_request_impl.register(HttpController, AddLearningRequestView)
