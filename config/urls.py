from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static # new

urlpatterns = [
    path('', include('src.store.urls')),
    path('users/', include('src.users.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
