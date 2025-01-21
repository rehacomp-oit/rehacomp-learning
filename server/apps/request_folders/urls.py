from django.urls import path

from .views import AddLearningRequestView, show_folders_list


app_name = 'request_folders'

urlpatterns = (
    path('', show_folders_list, name='folders'),
    path('new_request/', AddLearningRequestView.as_view(), name='register_request'),
)
