from django.contrib.admin import ModelAdmin, ShowFacets, site

from .models import Course, VOSOrganization


class ExtendedModelAdmin(ModelAdmin):
    show_facets = ShowFacets.NEVER


site.register(VOSOrganization, ExtendedModelAdmin)
site.register(Course, ExtendedModelAdmin)
