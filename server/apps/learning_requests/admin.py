from django.contrib.admin import ModelAdmin, ShowFacets, site

from .models import Course, VOSOrganization


class ExtendedModelAdmin(ModelAdmin):
    show_facets = ShowFacets.NEVER


class CourseAdmin(ExtendedModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


site.register(VOSOrganization, ExtendedModelAdmin)
site.register(Course, CourseAdmin)
