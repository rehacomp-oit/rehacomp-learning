from dataclasses import dataclass

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET
from returns.result import Failure, Success
from server.common.django_tools import htmx_render as render
from server.common.django_tools import HtmxHttpRequest

from .forms import LearningRequestForm
from .protocols.usecases import GetCourseFoldersListUseCase


@method_decorator((login_required, require_GET), name='__call__')
@dataclass(frozen=True, slots=True)
class GetFoldersListView:
    service: GetCourseFoldersListUseCase

    def __call__(self, request: HtmxHttpRequest) -> HttpResponse:
        page_template = 'folders_list.html'
        template_context = {}
        match self.service():
            case Success(value):
                template_context['folders'] = value
            case Failure():
                page_template = 'folders_not_found.html'

        return render(request, page_template, template_context)


@login_required
@require_GET
def add_request(request: HtmxHttpRequest) -> HttpResponse:
    data = {'learning_course': ((1, 'a'), (2, 'b'))}
    form = LearningRequestForm(initial=data)
    return render(request, 'add_request.html', {'form': form})
