from typing import Final, final

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.views.generic.base import View
from returns.result import Failure, Success
from server.apps.request_folders.protocols.services import ShowCourseFoldersListUseCase
from server.common.django_tools import htmx_render as render
from server.common.django_tools import HtmxHttpRequest


@final
class LoadFolderNamesView(LoginRequiredMixin, View):

    SUCCESS_PAGE: Final = 'folders_list.html'

    service: ShowCourseFoldersListUseCase = None  # type: ignore


    def __init__(self, *, service: ShowCourseFoldersListUseCase) -> None:
        self.service = service
        super().__init__()


    def get(self, request: HtmxHttpRequest) -> HttpResponse:
        template_context: dict[str, tuple[()]] = {}
        match self.service():
            case Success(value):
                template_context['folders'] = value
                return render(request, self.SUCCESS_PAGE, template_context)

            case Failure():
                raise Http404()
