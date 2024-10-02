from typing import final

from django.contrib.admin import ModelAdmin, register, ShowFacets
from django.db.models import Model
from django.forms import CharField, ModelForm
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from ulid import new as new_ULID

from .models import Course, VOSOrganization


@final
class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'slug',)


    name = CharField(
        label=_('Course name'),
        help_text=_('Full name of the course'),
        min_length=2,
        required=True,
        strip=True
    )
    slug = CharField(required=True)


    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['slug'].widget.attrs['readonly'] = True


@final
class VOSOrganizationForm(ModelForm):
    class Meta:
        model = VOSOrganization
        fields = ('organization_name',)


    organization_name = CharField(
        label=_('organization_name'),
        required=True,
        strip=True
    )


class GenericModelAdmin(ModelAdmin):
    '''
    Base class for registering orm models in the admin panel.

    It defines the general behavior and a set of properties for representing the model.
    '''

    show_facets = ShowFacets.NEVER


    def save_model(
        self,
        request: HttpRequest,
        obj: Model,
        form: ModelForm,
        change: bool
    ):
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
