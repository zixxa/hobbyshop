from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('signin/', LoginView.as_view(template_name="users/signin.html"), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.logout, name='logout'),
]
