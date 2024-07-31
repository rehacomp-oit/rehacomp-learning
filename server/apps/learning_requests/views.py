from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@login_required
@require_http_methods(('GET',))
def show_learning_requests(request: HttpRequest) -> HttpResponse:
    '''
Main (or index) view of this application.

    Returns rendered page with list of learning requests.
    '''

    return render(request, 'learning_requests/main.html')
