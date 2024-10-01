from typing import final

from django.contrib.admin import ModelAdmin, register, ShowFacets
from server.apps.request_folders.models import Course, VOSOrganization
from ulid import new as new_ULID

from .forms import CourseForm, VOSOrganizationForm


class GenericModelAdmin(ModelAdmin):
    show_facets = ShowFacets.NEVER


    def save_model(self, request, obj, form, change):
        obj.id = new_ULID()
        super().save_model(request, obj, form, change)


@register(Course)
@final
class CourseAdmin(GenericModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    form = CourseForm


@register(VOSOrganization)
class VOSOrganizationAdmin(GenericModelAdmin):
    form = VOSOrganizationForm
