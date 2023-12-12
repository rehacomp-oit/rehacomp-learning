from django.http import HttpRequest, HttpResponse


# fake view because this do nothing.
def index(request: HttpRequest) -> HttpResponse:
    '''
Main (or index) view.
    Returns rendered default page to the user.
    '''
    content = '<br><h1>Hello, world</h1><br>'
    return HttpResponse(content)
