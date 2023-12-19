from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import RegisterForm


login_user = LoginView.as_view(
    template_name='accounts/login.html',
    next_page=reverse_lazy('main:profile'),
)


def register_user(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
