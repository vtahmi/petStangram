from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from petStangram.accounts.forms import AppUserCreationForm, AppUserChangeForm
from petStangram.accounts.models import Profile

UserModel = get_user_model()

@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    model = UserModel
    ordering = ('pk',)
    list_display = ('email', 'is_staff', 'is_superuser', 'is_active')
    add_form = AppUserCreationForm
    form = AppUserChangeForm

    fieldsets = (
        (None, {
            "fields": ("email", "password"),
        }),
        (("Permissions"), {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            ),
        }),
        (("Important dates"), {
            "fields": ("last_login",),
        }),
    )
    add_fieldsets = (
        (None, {
            "fields": ("email", "password1", "password2"),
        }),
    )



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('user',)
