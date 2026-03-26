from django.urls import path

from petStangram.common import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('like/<int:photo_id>/', views.like, name='like-photo'),
    path('share/<int:photo_id>/', views.share_photo, name='share-photo'),
    path('add/<int:photo_id>/comment/', views.add_comment, name='add-comment'),
]