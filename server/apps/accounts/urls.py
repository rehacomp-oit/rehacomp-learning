from django.urls import path

from .views import LogOutUserView, show_profile_page, SignInView, SignupView


app_name = 'accounts'

urlpatterns = (
    path('register/', SignupView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('profile/', show_profile_page, name='profile'),
    path('logout/', LogOutUserView.as_view(), name='logout'),
)
