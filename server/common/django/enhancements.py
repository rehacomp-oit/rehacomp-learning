'''
A set of customizations for django.
'''

from typing import Any, final, MutableMapping
from typing import Final as Constant

from django.http import HttpRequest, HttpResponse
from django.template import loader
from django_htmx.middleware import HtmxDetails


GENERIC_BASE: Constant = 'main/_base.html'
PARTIAL_BASE: Constant = 'main/_partial.html'


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
    template_name: str,
    context: MutableMapping[str, Any] | None=None,
    content_type: str | None=None,
    status: int | None=None,
    using: str | None=None,
) -> HttpResponse:
    '''
        Render a template with context data, supporting htmx.

    This function overloads the `render` function from `django.shortcuts` to provide
    HTML rendering capabilities that integrate with htmx for dynamic client-side interactions.
    '''

    rendering_context = context or {}
    rendering_context['base_template'] = PARTIAL_BASE if request.htmx else GENERIC_BASE
    html = loader.render_to_string(template_name, rendering_context, request, using=using)
    return HttpResponse(html, content_type, status)
