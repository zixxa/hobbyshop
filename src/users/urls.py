from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('signin/', LoginView.as_view(template_name="users/signin.html"), name='login'),
    path('signup/', views.signup, name='signup'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
]
