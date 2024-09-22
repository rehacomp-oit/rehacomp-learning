from typing import final

from django.forms import CharField, ModelForm
from django.utils.translation import gettext_lazy as _
from server.apps.request_folders.models import Course, VOSOrganization


@final
class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'short_name', 'slug',)


    name = CharField(
        label=_('Course name'),
        help_text=_('Full name of the course'),
        min_length=2,
        required=True,
        strip=True
    )
    short_name = CharField(
        label=_('Abbreviation'),
        min_length=1,
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
