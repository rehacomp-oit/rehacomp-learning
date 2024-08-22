from django.urls import path

from .registry import folder_list_service_impl
from .protocols.services import CourseFoldersListUseCase
from .views import ShowFolderContentView, ShowFoldersView


app_name = 'learning_requests'

urlpatterns = (
    path(
        '',
        ShowFoldersView.as_view(folder_list_service=folder_list_service_impl.resolve(CourseFoldersListUseCase)),
        name='requests'
    ),

    path(
        'folder',
        ShowFolderContentView.as_view(),
        name='folder'
    ),
)
