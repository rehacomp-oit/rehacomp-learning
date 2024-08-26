from django.urls import path

from .protocols.services import CourseFoldersListUseCase
from .registry import folder_list_service_impl
from .views import ShowFolderContentView, ShowFoldersView


app_name = 'learning_requests'

_show_folders = ShowFoldersView.as_view(service=folder_list_service_impl.resolve(CourseFoldersListUseCase))
_get_learning_requests = ShowFolderContentView.as_view()


urlpatterns = (
    path('', _show_folders, name='folders'),
    path('folder_<int:course_id>/', _get_learning_requests, name='folder'),
)
