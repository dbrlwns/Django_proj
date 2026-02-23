from django.contrib.auth import logout, login, authenticate
from django.contrib.messages import error
from django.shortcuts import render, redirect

from users.forms import RegisterForm
from users.models import User
import logging

logger = logging.getLogger("auth")

# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            logger.info(f"{request.user} LOGIN")
            return redirect('/')
        else:
            error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')


def user_logout(request):
    if request.user.is_authenticated:
        logger.info(f"{request.user} LOGOUT")
        logout(request)
        return redirect('/')
    return redirect('/')

def user_register(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = RegisterForm(request.POST or None)
    print(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        logger.info(f"{request.user} REGISTERED")
        return redirect('/user/')
    return render(request, 'users/register.html',
                  {'form': form})

