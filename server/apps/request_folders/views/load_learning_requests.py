from typing import Final, final

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic.base import View
from server.apps.request_folders.protocols.repositories import CourseRepository
from server.common.django_tools import htmx_render as render
from server.common.django_tools import HtmxHttpRequest


@final
class LoadLearningRequestsView(LoginRequiredMixin, View):

    PAGE_TEMPLATE: Final = 'folder.html'

    repository: CourseRepository = None  # type: ignore


    def __init__(self, *, repository: CourseRepository) -> None:
        self.repository = repository
        super().__init__()


    def get(self, request: HtmxHttpRequest, folder_slug: str) -> HttpResponse:
        template_context = {'current_folder_slug': folder_slug}
        folder_name = self.repository.fetch_course_name_by_slug(folder_slug)
        if folder_name:
            template_context['current_folder_name'] = folder_name

        return render(request, self.PAGE_TEMPLATE, template_context)
