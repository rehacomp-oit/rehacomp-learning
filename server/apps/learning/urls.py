from django.urls import path

from .views import index


app_name = 'learning'

urlpatterns = (
    path('profile/', index, name='profile'),
)
