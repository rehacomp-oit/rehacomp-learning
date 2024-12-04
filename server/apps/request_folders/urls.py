from django.urls import path
from server.common.protocols import HttpController

from .registry import add_learning_request_impl, folder_list_service_impl


app_name = 'request_folders'

urlpatterns = (
    path('', folder_list_service_impl.resolve(HttpController), name='folders'),
    path('new_request/', add_learning_request_impl.resolve(HttpController), name='register_request'),
)
