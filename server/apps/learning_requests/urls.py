from django.urls import path

from .infrastructure.repositories import CourseDBRepo
from .protocols.services import ShowCourseFoldersListUseCase
from .registry import folder_list_service_impl
from .views import LoadFolderNamesView, LoadLearningRequestsView


app_name = 'learning_requests'

_load_folder_names = LoadFolderNamesView.as_view(service=folder_list_service_impl.resolve(ShowCourseFoldersListUseCase))
_load_learning_requests = LoadLearningRequestsView.as_view(repository=CourseDBRepo())


urlpatterns = (
    path('', _load_folder_names, name='folders'),
    path('<slug:folder_slug>/', _load_learning_requests, name='folder'),
)
