from punq import Container

from .protocols.repositories import CourseRepository
from .protocols.services import CourseFoldersListUseCase
from .repositories import CourseDBRepo
from .services import CourseFoldersListService


folder_list_service_impl = Container()
folder_list_service_impl.register(CourseRepository, CourseDBRepo)
folder_list_service_impl.register(CourseFoldersListUseCase, CourseFoldersListService)
