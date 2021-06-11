from django.urls import path
from .views import ItemView
from . import views

urlpatterns = [
    path('', views.index),
    path('items/<item_slug>/', views.item_page, name='content_item'),
    path('category/<parent_slug>/', views.category_list, name='parent_category'),
    path('category/<parent_slug>/<category_slug>/', views.item_list, name='content_category'),
    path('api', ItemView.as_view())
]
