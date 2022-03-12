from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static # new
from django.contrib.auth.views import LogoutView
from rest_framework import routers
from src.store import views

router = routers.DefaultRouter()
router.register(r'itemset', views.ItemViewSet, basename='Item')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('src.store.urls')),
    path('users/', include('src.users.urls')),
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name='logout'),
]


if settings.DEBUG: # new
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
