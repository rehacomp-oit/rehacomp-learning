from punq import Container

from .infrastructure.repositories import CourseDBRepo
from .protocols.repositories import CourseRepository
from .protocols.services import CourseFoldersListUseCase
from .services import CourseFoldersListService


folder_list_service_impl = Container()
folder_list_service_impl.register(CourseRepository, CourseDBRepo)
folder_list_service_impl.register(CourseFoldersListUseCase, CourseFoldersListService)
