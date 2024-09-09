from typing import Final, final

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.views.generic.base import View
from returns.result import Failure, Success
from server.apps.learning_requests.protocols.results import FolderListFailure
from server.apps.learning_requests.protocols.services import CourseFoldersListUseCase
from server.common.django_tools import htmx_render as render
from server.common.django_tools import HtmxHttpRequest


@final
class LoadFolderNamesView(LoginRequiredMixin, View):

    SUCCESS_PAGE: Final = 'folders_list.html'
    UNSUCCESS_PAGE: Final = 'empty_folders_list.html'

    service: CourseFoldersListUseCase = None  # type: ignore


    def __init__(self, *, service: CourseFoldersListUseCase) -> None:
        self.service = service
        super().__init__()


    def get(self, request: HtmxHttpRequest) -> HttpResponse:
        template_context: dict[str, tuple[()]] = {}
        match self.service():
            case Success(value):
                template_context['folders'] = value
                return render(request, self.SUCCESS_PAGE, template_context)

            case Failure(FolderListFailure.EMPTY_LIST):
                return render(request, self.UNSUCCESS_PAGE, template_context)

            case Failure(FolderListFailure.BROKEN_FOLDER_NAME):
                raise Http404()
