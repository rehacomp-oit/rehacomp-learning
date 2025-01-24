from typing import final

from django.http import HttpRequest
from django_htmx.middleware import HtmxDetails


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
