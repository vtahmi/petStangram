from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

UserModel = get_user_model()
class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)

class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'

class AppUserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
