from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from server.utilites.django_tools import HtmxHttpRequest


# fake view because this do nothing.
@login_required
@require_GET
def show_main_page(request: HtmxHttpRequest) -> HttpResponse:
    '''
Main (or index) view.
    Returns rendered default page to the user.
    '''
    return render(request, 'main/index.html')
