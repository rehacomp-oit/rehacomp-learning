'''
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.
'''

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


# Serving text and xml static files:
__robots_view = TemplateView.as_view(
    template_name='txt/robots.txt',
    content_type='text/plain',
)

__humans_view = TemplateView.as_view(
    template_name='txt/humans.txt',
    content_type='text/plain',
)


urlpatterns = (
    path('admin/', admin.site.urls),
    path('robots.txt', __robots_view),
    path('humans.txt', __humans_view),
)
