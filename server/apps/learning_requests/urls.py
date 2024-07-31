from django.urls import path

from .views import show_learning_requests


app_name = 'learning_requests'

urlpatterns = (
    path('', show_learning_requests, name='requests'),
)
