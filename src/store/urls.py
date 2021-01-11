from django.urls import path
from .views import ItemView
from . import views

urlpatterns = [
    path('', views.index),
    path('items/<item_slug>/', views.item_page, name='content_item'),
    path('api', ItemView.as_view())
]
