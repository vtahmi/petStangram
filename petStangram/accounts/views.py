from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Count, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView

from petStangram.accounts.forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm
from petStangram.accounts.models import Profile

UserModel = get_user_model()

class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class AppUserLoginView(LoginView):
    form_class = AppUserLoginForm
    template_name = 'accounts/login-page.html'


class AppUserLogoutView(LogoutView):
    template_name = 'accounts/logout-page.html'


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse('profile-details', kwargs={'pk': self.object.pk})

class ProfileDetailsView(LoginRequiredMixin ,DetailView):
    model = Profile
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_likes'] = self.object.user.photo_set.annotate(num_likes=Count('like')).aggregate(total_likes=Sum('num_likes'))['total_likes'] or 0
        context['pets_count'] = self.object.user.pet_set.count()
        context['photos_count'] = self.object.user.photo_set.count()

        return context

def profile_delete(request, pk):
    return render(request, 'accounts/profile-delete-page.html', {'pk': pk})

def profile_details(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    context = {'profile': profile}
    return render(request, 'accounts/profile-details-page.html', context)

