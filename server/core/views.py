'''
Serving text and xml static files.
'''

from typing import final

from django.views.generic.base import TemplateView


@final
class RobotsView(TemplateView):
    template_name: str | None = 'common/txt/robots.txt'
    content_type: str | None = 'text/plain'


@final
class HumansView(TemplateView):
    template_name: str | None = 'common/txt/humans.txt'
    content_type: str | None = 'text/plain'
