from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import UserFormRegister, UserFormLogin, UserFormUpdateAvatar
from django.utils.translation import ugettext_lazy as _
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
      user = user_form.save(commit=False)
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


@login_required
def user_change_password(request):
  if request.method == "POST":
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
      messages.success(request, _('Your password was successfully updated!'))
      return redirect('user_profile')
    else:
      messages.error(request, _('Please correct the error below.'))
      return redirect('user_change_password')
  return render(request, 'changepassword.html', {'form': PasswordChangeForm(request.user), 'layout': get_layout()})


@login_required
def user_change_avatar(request):
  if request.method == "POST":
    form = UserFormUpdateAvatar(request.POST, request.FILES)
    print(request.POST.get('password'), request.POST.get('avatar'))
    if form.is_valid():
      if request.user.check_password(form.cleaned_data['password']):
        avatar = form.cleaned_data['avatar']
        print(avatar)
        request.user.avatar = avatar
        messages.success(request, _('Your password was successfully updated!'))
        request.user.save()
        return redirect('user_profile')

    messages.error(request, _('Please correct the error below.'))
    return redirect('user_change_avatar')

  return render(request, 'user_change_avatar.html', {
    'form': UserFormUpdateAvatar(),
    'layout': get_layout()
  })
