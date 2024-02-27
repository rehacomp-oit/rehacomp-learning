from typing import Final

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


LOGIN_SUCCESS_URL_NAME: Final = 'main:profile'
LOGIN_PAGE_TEMPLATE_NAME: Final = 'accounts/login.html'


login_user = LoginView.as_view(
    template_name=LOGIN_PAGE_TEMPLATE_NAME,
    next_page=reverse_lazy(LOGIN_SUCCESS_URL_NAME),
)
