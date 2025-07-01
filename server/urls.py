'''
Main URL mapping configuration module.

Include other URLConfs from external apps using method `include()`.
'''

from __future__ import annotations

from typing import TYPE_CHECKING

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from health_check import urls as health_urls
from server.apps.accounts import urls as accounts_urls
from server.apps.accounts.presentation.views import show_profile_page

from .core.views import HumansView, RobotsView

if TYPE_CHECKING:
    from django.urls.resolvers import URLPattern, URLResolver


admin.autodiscover()


urlpatterns: tuple[URLResolver | URLPattern, ...] = (
    path('accounts/', include(accounts_urls, namespace='accounts')),
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
