from enum import StrEnum, unique
from typing import Any, final, MutableMapping, Sequence

from django.http import HttpResponse
from django.template import loader

from .http import HtmxHttpRequest


@final
@unique
class TemplatePath(StrEnum):
    GENERIC_BASE = 'main/_base.html'
    PARTIAL_BASE = 'main/_partial.html'
    MAIN_PAGE = 'main/index.html'
    LOGIN_PAGE = 'accounts/login.html'
    REGISTRATION_PAGE = ''


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
    '''

    rendering_context = context or {}
    if request.htmx:
        rendering_context['base_template'] = TemplatePath.PARTIAL_BASE.value
    else:
        rendering_context['base_template'] = TemplatePath.GENERIC_BASE.value

    content = loader.render_to_string(template_name, rendering_context, request, using=using)
    return HttpResponse(content, content_type, status)
