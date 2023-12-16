'''
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.
'''

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from health_check import urls as health_urls
# from server.apps.accounts import urls as accounts_urls
from server.apps.main import urls as main_urls
from server.apps.main.views import index


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
    # path('accounts/', include(accounts_urls)),
    path('main/', include(main_urls, namespace='main')),
    path('health/', include(health_urls)),
    path('admin/', admin.site.urls),
    path('robots.txt', __robots_view),
    path('humans.txt', __humans_view),
    # Explicit index view:
    path('', index, name='index'),
)
