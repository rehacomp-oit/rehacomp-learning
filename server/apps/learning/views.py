from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# fake view because this do nothing.
@login_required
def index(request: HttpRequest) -> HttpResponse:
    '''
Main (or index) view.
    Returns rendered default page to the user.
    '''
    return render(request, 'learning/index.html')
