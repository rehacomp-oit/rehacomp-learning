from django.urls import path
from server.common.protocols import HttpController

from .registry import folder_list_service_impl
from .views import add_request


app_name = 'request_folders'

urlpatterns = (
    path('', folder_list_service_impl.resolve(HttpController), name='folders'),
    path('new_request/', add_request, name='register_request'),
)
