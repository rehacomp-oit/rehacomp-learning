from django.urls import path

from .registry import folder_list_service_impl
from .views import add_request


app_name = 'request_folders'

urlpatterns = (
    path('', folder_list_service_impl.resolve('view'), name='folders'),
    path('new_request/', add_request, name='register_request'),
)
