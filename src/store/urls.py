from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('items/<item_slug>/', views.item_page, name='content_item'),
]
