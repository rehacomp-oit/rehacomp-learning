from typing import Final, final

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic.base import View
from server.common.django_tools import htmx_render as render
from server.common.django_tools import HtmxHttpRequest


@final
class LoadLearningRequestsView(LoginRequiredMixin, View):

    PAGE_TEMPLATE: Final = 'folder.html'


    def get(self, request: HtmxHttpRequest, folder_slug: str) -> HttpResponse:
        template_context: dict[str, object] = {}
        return render(request, self.PAGE_TEMPLATE, template_context)
