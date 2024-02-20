from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexItemList.as_view(), name="content_items"),
    path('items/<slug:item_slug>/', views.ItemDetail.as_view(), name='content_item'),
    path('category/<slug:category_slug>/', views.CategoryList.as_view(), name='content_category'),

    path("", views.cart_detail, name="cart_detail"),
]
