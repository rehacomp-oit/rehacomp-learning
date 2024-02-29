from django.contrib.auth import authenticate, login
from django.contrib.messages import error
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from server.apps.accounts.forms import LoginForm

from .common_constants import LOGIN_PAGE_TEMPLATE_NAME, LOGIN_SUCCESS_URL_NAME


def __handle_get_request(request: HttpRequest) -> HttpResponse:
    form = LoginForm()
    return render(request, LOGIN_PAGE_TEMPLATE_NAME, {'form': form})


def __handle_post_request(
    request: HttpRequest
) -> HttpResponse | HttpResponseRedirect:
    form = LoginForm(request.POST)
    if form.is_valid():
        user = authenticate(request, **form.cleaned_data)
        if user is not None:
            login(request, user)
            return redirect(LOGIN_SUCCESS_URL_NAME)

    error(request, 'Не удалось войти в систему')
    return render(request, LOGIN_PAGE_TEMPLATE_NAME, {'form': form})


def login_user(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == 'POST':
        return __handle_post_request(request)

    return __handle_get_request(request)
