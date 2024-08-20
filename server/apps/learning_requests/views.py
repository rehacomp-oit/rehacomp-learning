from typing import Final, final

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from returns.result import Failure, Success
from server.apps.core.protocols.results import FolderListFailure
from server.apps.core.protocols.services import CourseFoldersListUseCase


@final
class ShowFoldersView(LoginRequiredMixin, View):

    SUCCESS_PAGE: Final = 'folders_list.html'
    UNSUCCESS_PAGE: Final = 'empty_folders_list.html'

    folder_list_service: CourseFoldersListUseCase = None  # type: ignore


    def __init__(self, *, folder_list_service: CourseFoldersListUseCase) -> None:
        self.folder_list_service = folder_list_service
        super().__init__()


    def get(self, request: HttpRequest) -> HttpResponse:
        template_context: dict[str, tuple[()]] = {}
        match self.folder_list_service():
            case Success(value):
                template_context['folders'] = value
                return render(request, self.SUCCESS_PAGE, template_context)

            case Failure(FolderListFailure.EMPTY_LIST):
                return render(request, self.UNSUCCESS_PAGE, template_context)

            case Failure(FolderListFailure.BROKEN_FOLDER_NAME):
                raise Http404()


@final
class ShowFolderContentView(LoginRequiredMixin, View):

    PAGE_TEMPLATE: Final = 'folder.html'


    def get(self, request: HttpRequest, folder_name: str) -> HttpResponse:
        template_context = {'folder_name': folder_name}
        return render(request, self.PAGE_TEMPLATE, template_context)
