from django.urls import path

from .views import show_main_page


app_name = 'core'

urlpatterns = (
    path('', show_main_page, name='profile'),
)
