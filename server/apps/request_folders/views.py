from dataclasses import dataclass
from typing import final

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET, require_http_methods
from returns.result import Failure, Success
from server.common.django_tools import htmx_render as render
from server.common.django_tools import HtmxHttpRequest
from server.common.exceptions import ControllerError

from .domain.protocols.usecases import GetCourseFoldersUsecase, GetRequestFormOptionsUsecase
from .domain.results import GetCourseFoldersFailure, GetRequestFormOptionFailure
from .forms import LearningRequestForm


@final
@method_decorator((login_required, require_GET), name='__call__')
@dataclass(frozen=True, slots=True)
class GetFoldersListView:
    get_folders_list: GetCourseFoldersUsecase

    def __call__(self, request: HtmxHttpRequest) -> HttpResponse:
        match self.get_folders_list():
            case Success(value):
                template_context = {'folders': value}
                page_template = 'folders_list.html'
                return render(request, page_template, template_context)
            case Failure(GetCourseFoldersFailure.MISSING_DATA):
                page_template = 'folders_not_found.html'
                return render(request, page_template)
            case Failure(_):
                raise ControllerError('Error')


@final
@method_decorator((login_required, require_http_methods(('GET', 'POST')),), name='__call__')
@dataclass(frozen=True, slots=True)
class AddLearningRequestView:
    get_request_form_options: GetRequestFormOptionsUsecase


    def __call__(self, request: HtmxHttpRequest) -> HttpResponse:
        return self._handle_GET(request)


    def _handle_GET(self, request: HtmxHttpRequest) -> HttpResponse:
        match self.get_request_form_options():
            case Success(value):
                form = LearningRequestForm.build_unbound_form(
                    value.course_choices,
                    value.organization_choices
                )
                return render(request, 'add_request.html', {'form': form})
            case Failure(GetRequestFormOptionFailure.MISSING_DATA):
                page_template = 'folders_not_found.html'
                return render(request, page_template)
            case Failure(_):
                raise ControllerError('Error')
