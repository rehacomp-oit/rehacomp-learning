from django.contrib.auth import logout
from django.contrib.messages import success
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect

from .common_constants import REGISTER_SUCCESS_URL_NAME


def logout_user(request: HttpRequest) -> HttpResponseRedirect:
    logout(request)
    success(request, 'Вы вышли из системы')
    return redirect(REGISTER_SUCCESS_URL_NAME)
