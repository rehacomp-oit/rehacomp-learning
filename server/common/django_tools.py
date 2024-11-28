'''
A set of customizations for django.
'''

from typing import Any, final, MutableMapping, Sequence
from uuid import UUID

from django.contrib.admin import ModelAdmin, ShowFacets
from django.core.exceptions import ValidationError
from django.db.models.fields import Field
from django.http import HttpRequest, HttpResponse
from django.template import loader
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
    '''
    An HttpRequest subclass that enhances the standard Django request object
    with additional attributes for htmx support.

    This class is primarily intended for type annotations and is not meant
    to be instantiated directly. It extends the standard HttpRequest to
    include htmx-specific details that may be useful when handling
    htmx requests in Django views.

    Attributes:
        htmx: An instance of HtmxDetails that contains
        specific information about the htmx request, such as the request
        method, headers, and relevant attributes that help in processing
        htmx-driven interactions.

    Note:
        This class should be used to annotate views that expect htmx
        requests, providing better type hints and improving code readability.
    '''

    htmx: HtmxDetails


def htmx_render(
    request: HtmxHttpRequest,
    template_name: str | Sequence[str],
    context: MutableMapping[str, Any] | None=None,
    content_type: str | None=None,
    status: int | None=None,
    using: str | None=None,
) -> HttpResponse:
    '''
        Render a template with context data, supporting htmx.

    This function overloads the `render` function from `django.shortcuts` to provide
    HTML rendering capabilities that integrate with htmx for dynamic client-side interactions.

    Parameters:
        request: The HTTP request object, extended to support htmx attributes.
        template_name: The name of the template to be rendered, or a sequence of template names.
        context: A dictionary of context data to pass to the template. Defaults to None.
        content_type: The MIME type to use for the response. Defaults to None.
        status: The HTTP status code to return. Defaults to None.
        using: The name of the template engine to use. Defaults to None.

    Returns:
        HttpResponse: The rendered template as an HttpResponse object.

    Raises:
        TemplateDoesNotExist: If the template is not found.
        SuspiciousOperation: If the request is not valid for htmx rendering.
'''

    rendering_context = context or {}
    rendering_context['base_template'] = 'main/_partial.html' if request.htmx else 'main/_base.html'
    content = loader.render_to_string(template_name, rendering_context, request, using=using)
    return HttpResponse(content, content_type, status)
