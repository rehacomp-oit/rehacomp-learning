'''
Serving text and xml static files.
'''

from typing import final

from django.views.generic.base import TemplateView


@final
class RobotsView(TemplateView):
    template_name = 'common/txt/robots.txt'
    content_type = 'text/plain'


@final
class HumansView(TemplateView):
    template_name = 'common/txt/humans.txt'
    content_type = 'text/plain'
