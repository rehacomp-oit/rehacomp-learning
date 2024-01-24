from django.urls import path

from .views import login_user, register_user


app_name = 'accounts'

urlpatterns = (
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
)
