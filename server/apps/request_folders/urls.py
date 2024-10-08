from django.urls import path

from .views import load_folders_names


app_name = 'request_folders'

urlpatterns = (
    path('', load_folders_names, name='folders'),
)
