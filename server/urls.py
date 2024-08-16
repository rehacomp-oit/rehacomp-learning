'''
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.
'''

from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from health_check import urls as health_urls
from server.apps.accounts import urls as accounts_urls
from server.apps.learning_requests import urls as learning_request_urls
from server.apps.main import urls as main_urls
from server.apps.main.views import show_main_page


# Customizing the admin panel via a global admin site object
admin.site.site_title = _('Admin panel')
admin.site.site_header = _('The admin panel of the rehacomp-learning service.')
admin.site.index_title = _('Home page')
admin.site.unregister(Group)


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
    path('accounts/', include(accounts_urls, namespace='accounts')),
    path('learning_requests/', include(learning_request_urls, namespace='learning_requests')),
    path('main/', include(main_urls, namespace='main')),
    path('health/', include(health_urls)),
    path('admin/', admin.site.urls),
    path('robots.txt', __robots_view),
    path('humans.txt', __humans_view),
    # Explicit index view:
    path('', show_main_page, name='index'),
)
