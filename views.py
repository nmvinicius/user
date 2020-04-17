from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserFormRegister, UserFormLogin
import os


def get_layout() -> str:
    if os.path.exists('templates/baseLayout.html'):
        return 'baseLayout.html'
    else:
        return 'baseNone.html'


def user_register(request):
    if request.method == "POST":
        user_form = UserFormRegister(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, authenticate(email=request.POST.get('email'), password=request.POST.get('password')))
            return redirect('user_profile')
    return render(request, 'register.html', {"form": UserFormRegister(), "layout": get_layout()})


@login_required
def user_profile(request):
    return render(request, 'profile.html', {"layout": get_layout()})


@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')


@login_required
def user_delete(request):
    User.objects.get(pk=request.user.pk).delete()
    return redirect('user_register')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('user_profile')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('user_profile')
        return redirect('user_login')
    return render(request, 'login.html', {"form": UserFormLogin(), "users": User.objects.all(), "layout": get_layout()})
