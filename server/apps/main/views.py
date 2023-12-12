from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# fake view because this do nothing.
def index(request: HttpRequest) -> HttpResponse:
    '''
Main (or index) view.
    Returns rendered default page to the user.
    '''
    return render(request, 'main/index.html')
