from typing import final

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View
from django.views.decorators.http import require_GET
from returns.result import Failure, Success
from server.common.django_tools import htmx_render as render
from server.common.django_tools import HtmxHttpRequest
from server.common.exceptions import ControllerError

from .domain.protocols.usecases import GetCourseListUsecase, GetRequestFormOptionsUsecase
from .domain.results import GetCourseFoldersFailure, GetRequestFormOptionFailure
from .forms import LearningRequestForm
from .registry import course_list_container, request_form_options_container


@login_required
@require_GET
def show_folders_list(request: HtmxHttpRequest) -> HttpResponse:
    success_page, not_found_page = 'folders_list.html', 'folders_not_found.html'
    get_folders_list = course_list_container.resolve(GetCourseListUsecase)
    match get_folders_list():
        case Success(value):
            return render(request, success_page, {'folders': value})
        case Failure(GetCourseFoldersFailure.MISSING_DATA):
            return render(request, not_found_page)
        case Failure(_):
            raise ControllerError('Error')


@final
class AddLearningRequestView(LoginRequiredMixin, View):

    def get(self, request: HtmxHttpRequest) -> HttpResponse:
        get_request_form_options = request_form_options_container.resolve(GetRequestFormOptionsUsecase)
        match get_request_form_options():
            case Success(value):
                form = LearningRequestForm.build_unbound_form(**value.to_dict())
                return render(request, 'add_request.html', {'form': form})
            case Failure(GetRequestFormOptionFailure.MISSING_DATA):
                page_template = 'folders_not_found.html'
                return render(request, page_template)
            case Failure(_):
                raise ControllerError('Error')
