from typing import Final, TypeAlias

from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_http_methods

from .forms import LoginForm, RegisterForm
from .logic.exceptions import AccountAlreadyExists, MismatchedPasswords, UncorrectPassword
from .logic.implemented import signup_implementation


LOGIN_SUCCESS_URL_NAME: Final = 'core:profile'
LOGIN_PAGE_TEMPLATE_NAME: Final = 'accounts/login.html'
REGISTER_SUCCESS_URL_NAME: Final = 'accounts:login'
REGISTRATION_PAGE_TEMPLATE_NAME: Final = 'accounts/register.html'

ViewResponse: TypeAlias = HttpResponse | HttpResponseRedirect


@require_http_methods(('GET', 'POST',))
def login_user(request: HttpRequest) -> ViewResponse:
    if request.method == 'GET':
        form = LoginForm()
        return render(request, LOGIN_PAGE_TEMPLATE_NAME, {'form': form})

    form = LoginForm(request.POST)
    if not form.is_valid():
        return render(request, LOGIN_PAGE_TEMPLATE_NAME, {'form': form})

    user = authenticate(request, **form.cleaned_data)
    if user is None:
        return render(request, LOGIN_PAGE_TEMPLATE_NAME, {'form': form})

    login(request, user)
    return redirect(LOGIN_SUCCESS_URL_NAME)


def logout_user(request: HttpRequest) -> HttpResponseRedirect:
    logout(request)
    return redirect(REGISTER_SUCCESS_URL_NAME)


@require_http_methods(('GET', 'POST',))
def register_user(request: HttpRequest) -> ViewResponse:
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, REGISTRATION_PAGE_TEMPLATE_NAME, {'form': form})

    form = RegisterForm(request.POST)
    if not form.is_valid():
        return render(request, REGISTRATION_PAGE_TEMPLATE_NAME, {'form': form})

    try:
        signup = signup_implementation.resolve('service')
        signup(form.cleaned_data)
    except MismatchedPasswords:
        form.add_error('password2', _('The entered passwords didn\'t match.'))
        return render(request, REGISTRATION_PAGE_TEMPLATE_NAME, {'form': form})
    except UncorrectPassword:
        return render(request, REGISTRATION_PAGE_TEMPLATE_NAME, {'form': form})
    except AccountAlreadyExists:
        form.add_error('username', 'Такой пользователь уже существует')
        return render(request, REGISTRATION_PAGE_TEMPLATE_NAME, {'form': form})
    else:
        return redirect(REGISTER_SUCCESS_URL_NAME)
