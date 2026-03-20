
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from petStangram import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('petStangram.accounts.urls')),
    path('', include('petStangram.common.urls')),
    path('pets/', include('petStangram.pets.urls')),
    path('photos/', include('petStangram.photos.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)