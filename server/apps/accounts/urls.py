from django.contrib.auth.views import LogoutView
from django.urls import path

from .presentation.views import show_profile_page, SignInView, SignupView


app_name = 'accounts'

urlpatterns = (
    path('register/', SignupView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('profile/', show_profile_page, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
)
