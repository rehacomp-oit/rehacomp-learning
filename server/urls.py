'''
Main URL mapping configuration module.

Include other URLConfs from external apps using method `include()`.
'''

from typing import Any

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from health_check import urls as health_urls
from server.apps.accounts.presentation import urls as accounts_urls
from server.apps.accounts.presentation.views import show_profile_page
from server.apps.request_folders import urls as request_folders_urls

from .common.django.views import HumansView, RobotsView


# Customizing the admin panel via a global admin site object
admin.site.site_title = _('Admin panel')
admin.site.site_header = _('The admin panel of the rehacomp-learning service.')
admin.site.index_title = _('Home page')
admin.site.unregister(Group)


urlpatterns: tuple[Any, ...] = (
    path('accounts/', include(accounts_urls, namespace='accounts')),
    path('request_folders/', include(request_folders_urls, namespace='request_folders')),
    path('health/', include(health_urls)),
    path('admin/', admin.site.urls),
    path('robots.txt', RobotsView.as_view()),
    path('humans.txt', HumansView.as_view()),
    # Explicit index view:
    path('', show_profile_page, name='index'),
)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = (
        path('__debug__/', include(debug_toolbar.urls)),
        *urlpatterns,
    )
