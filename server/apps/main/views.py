from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from server.common.django_tools import htmx_render as render
from server.common.django_tools import HtmxHttpRequest


@login_required
@require_GET
def show_main_page(request: HtmxHttpRequest) -> HttpResponse:
    '''
Main (or index) view.
    Returns rendered default page to the user.
    '''
    return render(request, 'main/index.html')
