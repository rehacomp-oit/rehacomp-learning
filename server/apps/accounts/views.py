from typing import final

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_GET
from django.views.generic import FormView
from server.common.django.enhancements import htmx_render as render
from server.common.django.enhancements import HtmxHttpRequest, HtmxTemplateResponse

from .application.dependency_injection import register_employee_container
from .application.exceptions import EmployeeAlreadyExists, InvalidPassword, MismatchedPasswords
from .application.protocols import RegisterEmployeeUsecase
from .forms import SignupForm


@final
class SignupView(FormView):
    template_name = 'accounts/register.html'
    response_class = HtmxTemplateResponse
    form_class = SignupForm
    success_url = reverse_lazy('accounts:login')


    def form_valid(self, form: SignupForm) -> HttpResponseRedirect:
        register_user = register_employee_container.resolve(RegisterEmployeeUsecase)

        try:
            account = register_user(form.output)
        except MismatchedPasswords as error:
            form.add_error('password2', _(error.reason))
            return self.form_invalid(form)
        except InvalidPassword:
            return self.form_invalid(form)
        except EmployeeAlreadyExists as error:
            form.add_error('email', _(error.reason))
            return self.form_invalid(form)
        else:
            return super().form_valid(form)


@final
class SignInView(LoginView):
    template_name = 'accounts/login.html'
    response_class = HtmxTemplateResponse
    next_page = reverse_lazy('accounts:profile')


@final
class LogOutUserView(LogoutView):
    template_name = 'accounts/logout.html'
    response_class = HtmxTemplateResponse


@login_required
@require_GET
def show_profile_page(request: HtmxHttpRequest) -> HttpResponse:
    '''
Main (or index) view.
    Returns rendered default page to the user.
    '''
    template = 'accounts/profile.html'
    return render(request, template)
