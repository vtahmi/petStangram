from django.urls import path, include

from petStangram.accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/<int:pk>/', include([
        path('delete/', views.profile_delete, name='profile-delete'),
        path('', views.profile_details, name='profile-details'),
        path('edit/', views.profile_edit, name='profile-edit'),
    ])),

]