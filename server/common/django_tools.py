'''
A set of customizations for django.
'''

from typing import Any, final, MutableMapping, Sequence
from uuid import UUID

from django.contrib.admin import ModelAdmin, ShowFacets
from django.core.exceptions import ValidationError
from django.db.models.fields import Field
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django_htmx.middleware import HtmxDetails
from ulid import parse, ULID


@final
class PKULIDField(Field):
    '''
    Django model field type for handling ULID's.

    This field type is natively stored in the DB as a UUID (when supported) and a string/varchar(26) otherwise.
    It can be used as a primary key.
    '''

    default_error_messages = {'invalid': _('"%(value)s" is not a valid ULID.')}
    description = _('Universally Unique Lexicographically Sortable Identifier')
    empty_strings_allowed = False


    def __init__(self, verbose_name: str | None=None, **kwargs) -> None:
        kwargs.setdefault('max_length', 26)
        super().__init__(verbose_name, **kwargs)


    def deconstruct(self) -> tuple[str, str, list[Any], dict[str, Any]]:
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs


    def get_internal_type(self) -> str:
        return 'UUIDField'


    def get_db_prep_value(
        self,
        value: Any,
        connection: Any,
        prepared: bool=False
    ) -> ULID | UUID | str | None:
        if value is None:
            return value

        if not isinstance(value, ULID):
            value = self.to_python(value)

        return value.uuid if connection.features.has_native_uuid_field else str(value)


    def from_db_value(self, value: Any, expression: Any, connection: Any) -> ULID | None:
        return self.to_python(value)


    def to_python(self, value: Any) -> ULID | None:
        if value is None:
            return value

        try:
            return parse(value)
        except (AttributeError, ValueError):
            raise ValidationError(self.error_messages['invalid'], code='invalid', params={'value': value})


@final
class BaseModelAdmin(ModelAdmin):
    '''
    Lightweight admin panel object with disable faceting entirely.

    In most cases, you should use it to register models.
    '''

    show_facets = ShowFacets.NEVER


@final
class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails


def htmx_render(
    request: HtmxHttpRequest,
    template_name: str | Sequence[str],
    context: MutableMapping[str, Any] | None=None,
    content_type: str | None=None,
    status: int | None=None,
    using: str | None=None,
) -> HttpResponse:
    if context is None:
        context = {}

    if request.htmx:
        context['base_template'] = 'main/_partial.html'
    else:
        context['base_template'] = 'main/_base.html'

    return render(request, template_name, context, content_type, status, using)
