from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


# fake view because this do nothing.
@login_required
@require_http_methods(('GET',))
def index(request: HttpRequest) -> HttpResponse:
    '''
Main (or index) view.
    Returns rendered default page to the user.
    '''
    return render(request, 'learning/index.html')
