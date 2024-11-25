from dataclasses import dataclass
from logging import Logger
from typing import final

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET
from server.common.django_tools import htmx_render as render
from server.common.django_tools import HtmxHttpRequest
from server.common.exceptions import ControllerError, InfrastructureLayerError, MissingDataError

from .forms import LearningRequestForm
from .protocols.repositories import CourseFolderRepository


@final
@method_decorator((login_required, require_GET), name='__call__')
@dataclass(frozen=True, slots=True)
class GetFoldersListView:
    logger_object: Logger
    storage: CourseFolderRepository

    def __call__(self, request: HtmxHttpRequest) -> HttpResponse:
        try:
            folders = self.storage.fetch_all()
        except MissingDataError:
            message = 'Information about courses could not be found in the system'
            self.logger_object.info(message)
            page_template = 'folders_not_found.html'
            return render(request, page_template)
        except InfrastructureLayerError as Exc:
            raise ControllerError('Error with data storage') from Exc
        else:
            template_context = {'folders': folders}
            page_template = 'folders_list.html'
            return render(request, page_template, template_context)


@login_required
@require_GET
def add_request(request: HtmxHttpRequest) -> HttpResponse:
    data = {'learning_course': ((1, 'a'), (2, 'b'))}
    form = LearningRequestForm(initial=data)
    return render(request, 'add_request.html', {'form': form})
