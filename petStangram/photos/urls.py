from django.urls import path, include

from petStangram.photos import views

urlpatterns = [
    path('add/', views.photo_add, name='photo-add'),
    path('<int:pk>/', include([
        path('', views.photo_details, name='photo-details'),
        path('edit/', views.PhotoEditView.as_view(), name='photo-edit'),
        path('delete/', views.photo_delete, name='photo-delete'),
    ])),

]
