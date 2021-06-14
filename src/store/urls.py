from django.urls import path
from .views import ItemView
from . import views

urlpatterns = [
    path('', views.index),
    path('items/<item_slug>/', views.item_page, name='content_item'),
    path('category/<parent_slug>/', views.category_list, name='parent_category'),
    path('category/<parent_slug>/<category_slug>/', views.item_list, name='content_category'),
    path('api', ItemView.as_view()),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
]
