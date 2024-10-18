from django.urls import path

from .views import add_request, load_folders_names


app_name = 'request_folders'

urlpatterns = (
    path('', load_folders_names, name='folders'),
    path('new_request/', add_request, name='register_request'),
)
