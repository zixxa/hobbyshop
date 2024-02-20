from django.views.generic import ListView, DetailView

from src.store.models import Item, Category
from rest_framework.viewsets import ViewSet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .mixins import DataMixin
from .models import Cart


class IndexItemList(ListView, DataMixin):
    model = Item
    template_name = "index.html"
    context_object_name = 'items'
    extra_context = {
        'title': 'Главная страница',
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        super(get_context_data)

    def get_queryset(self):
        return Item.objects.filter(is_show_on_index=True, active_on=True)


class ItemListInCategory(ListView):
    template_name = "item_list.html"
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.filter(category__id=self.request.GET('category_id', 0), active_on=True)


class ItemDetail(DetailView, DataMixin):
    model = Item
    template_name = 'products/new_item.html'
    context_object_name = 'item'
    slug_url_kwarg = 'item_slug'


class CategoryList(ListView, DataMixin):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'item'
    slug_url_kwarg = 'category_slug'


''' Управление корзиной '''


@login_required
def add_to_cart(request, product_id):
    cart_item = Cart.objects.filter(user=request.user, product=product_id).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Item added to your cart.")
    else:
        Cart.objects.create(user=request.user, product=product_id)
        messages.success(request, "Item added to your cart.")

    return redirect("cart:cart_detail")


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")

    return redirect("cart:cart_detail")


@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.quantity * item.product.price for item in cart_items)

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }

    return render(request, "cart/cart_detail.html", context)
