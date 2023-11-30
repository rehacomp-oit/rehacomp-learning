'''
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.
'''

from django.contrib import admin
from django.urls import path


urlpatterns = (
    path('admin/', admin.site.urls),
)
