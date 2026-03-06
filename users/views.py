from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from django.shortcuts import render, redirect

from users.forms import RegisterForm, UserUpdateForm
from users.models import User
import logging
from django.contrib import messages

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
            messages.error(request, "Username or password is incorrect")
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
    if request.method == "POST" and form.is_valid():
        form.save()
        logger.info(f"{request.user} REGISTERED")
        return redirect('/user/')
    return render(request, 'users/register.html',
                  {'form': form})


@login_required
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        pw_form = PasswordChangeForm(request.user, request.POST)
        if user_form.is_valid():
            user_form.save()
        old_pw = request.POST.get('old_password')
        new_pw1 = request.POST.get('new_password1')
        new_pw2 = request.POST.get('new_password2')
        if old_pw or new_pw1 or new_pw2:
            if pw_form.is_valid():
                user = pw_form.save()
                update_session_auth_hash(request, user) # 로그아웃 방지
        logger.info(f"{request.user} UPDATED")
        return redirect('/user/')
    else:
        user_form = UserUpdateForm(instance=request.user)
        pw_form = PasswordChangeForm(request.user)
    return render(request, 'users/profile_update.html',
                  {'user_form': user_form, 'pw_form': pw_form})