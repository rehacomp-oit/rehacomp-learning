from typing import final

from django.contrib.admin import ModelAdmin, register, ShowFacets
from server.apps.learning_requests.models import Course, VOSOrganization

from .forms import CourseForm, VOSOrganizationForm


class ExtendedModelAdmin(ModelAdmin):
    show_facets = ShowFacets.NEVER


@register(Course)
@final
class CourseAdmin(ExtendedModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    form = CourseForm


@register(VOSOrganization)
class VOSOrganizationAdmin(ExtendedModelAdmin):
    form = VOSOrganizationForm
