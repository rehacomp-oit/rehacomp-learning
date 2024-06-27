from django.contrib.admin import ModelAdmin, ShowFacets, site


from .models import VOSOrganization


class ExtendedModelAdmin(ModelAdmin):
    show_facets = ShowFacets.NEVER


site.register(VOSOrganization, ExtendedModelAdmin)
