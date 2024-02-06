from typing import Final

from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import RegisterForm


LOGIN_SUCCESS_URL_NAME: Final = 'main:profile'
REGISTER_SUCCESS_URL_NAME: Final = 'accounts:login'
REGISTRATION_PAGE_TEMPLATE_NAME: Final = 'accounts/register.html'
LOGIN_PAGE_TEMPLATE_NAME: Final = 'accounts/login.html'


login_user = LoginView.as_view(
    template_name=LOGIN_PAGE_TEMPLATE_NAME,
    next_page=reverse_lazy(LOGIN_SUCCESS_URL_NAME),
)


def __try_register_user(
    request: HttpRequest
) -> HttpResponse | HttpResponseRedirect:
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(REGISTER_SUCCESS_URL_NAME)

    return render(request, REGISTRATION_PAGE_TEMPLATE_NAME, {'form': form})


def register_user(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == 'POST':
        return __try_register_user(request)

    form = RegisterForm()
    return render(request, REGISTRATION_PAGE_TEMPLATE_NAME, {'form': form})
