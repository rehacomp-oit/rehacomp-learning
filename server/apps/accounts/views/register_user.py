from django.contrib.messages import error, success
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from server.apps.accounts.forms import RegisterForm
from server.apps.accounts.services import create_new_account
from server.exceptions import ServiceFailed

from .common_constants import (
    REGISTER_SUCCESS_URL_NAME,
    REGISTRATION_PAGE_TEMPLATE_NAME
)


def __handle_get_request(request: HttpRequest) -> HttpResponse:
    form = RegisterForm()
    return render(request, REGISTRATION_PAGE_TEMPLATE_NAME, {'form': form})


def __handle_post_request(
    request: HttpRequest
) -> HttpResponse | HttpResponseRedirect:
    form = RegisterForm(request.POST)
    if form.is_valid():
        try:
            result = create_new_account(form.cleaned_data)
        except ServiceFailed:
            form.add_error('username', 'Такой пользователь уже существует')
        else:
            success(request, f'Добро пожаловать, {result}')
            return redirect(REGISTER_SUCCESS_URL_NAME)

    error(request, 'Ошибка регистрации!')
    return render(request, REGISTRATION_PAGE_TEMPLATE_NAME, {'form': form})


def register_user(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == 'POST':
        return __handle_post_request(request)

    return __handle_get_request(request)
