from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from petStangram.accounts.forms import AppUserCreationForm, AppUserLoginForm
from petStangram.accounts.models import Profile

UserModel = get_user_model()

class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'

class AppUserLoginView(LoginView):
    form_class = AppUserLoginForm
    template_name = 'accounts/login-page.html'


class AppUserLogoutView(LogoutView):
    template_name = 'accounts/logout-page.html'

def profile_delete(request, pk):
    return render(request, 'accounts/profile-delete-page.html', {'pk': pk})

def profile_details(request, pk):
    return render(request, 'accounts/profile-details-page.html', {'pk': pk})

def profile_edit(request, pk):
    return render(request, 'accounts/profile-edit-page.html', {'pk': pk})