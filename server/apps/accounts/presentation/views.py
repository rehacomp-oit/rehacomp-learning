from typing import final, override

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.http import require_GET
from django.views.generic import FormView
from returns.result import Failure, Success
from server.apps.accounts.application.contracts import RegisterUserUsecase
from server.apps.accounts.application.failures import RegistrationFailure, RegistrationFailureKind
from server.core.di import get_di_container
from server.core.http import HtmxHttpRequest

from .forms import SignupForm
from .template_paths import AccountsTemplate


@final
class SignupView(FormView[SignupForm]):
    template_name: str | None = AccountsTemplate.REGISTER
    form_class: type[SignupForm] | None = SignupForm
    success_url = reverse_lazy('accounts:login')
    register_user: RegisterUserUsecase = get_di_container().resolve(RegisterUserUsecase)


    @override
    def form_valid(self, form: SignupForm) -> HttpResponse:
        match self.register_user.execute(form.output):
            case Success(_): return super().form_valid(form)
            case Failure(error): return self._map_errors(form, error)
            case _: raise RuntimeError


    def _map_errors(
        self,
        form: SignupForm,
        failure_type: RegistrationFailure
    ) -> HttpResponse:
        match failure_type.kind:
            case RegistrationFailureKind.MISMATCHED_PASSWORDS:
                form.set_mismatched_passwords_error()
            case RegistrationFailureKind.INVALID_PASSWORD:
                form.set_password_validation_error(failure_type.details)
            case RegistrationFailureKind.ACCOUNT_ALREADY_EXISTS:
                form.set_account_already_exists_error()

        return self.form_invalid(form)


@final
class SignInView(LoginView):
    template_name: str | None = AccountsTemplate.LOGIN


@login_required
@require_GET
def show_profile_page(request: HtmxHttpRequest) -> HttpResponse:
    '''
Main (or index) view.
    Returns rendered default page to the user.
    '''
    return render(request, AccountsTemplate.PROFILE)
