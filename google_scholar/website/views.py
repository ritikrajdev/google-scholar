from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm


def index(request: HttpRequest):
    return render(request, 'website/base.html')


login = LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=True)
logout = LogoutView.as_view(template_name='registration/logout.html')


def register(request: HttpRequest):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', context={'form': form})
