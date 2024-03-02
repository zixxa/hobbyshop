from django.views.generic import ListView, DetailView

from src.store.models import Item, Category
from rest_framework.viewsets import ViewSet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .mixins import ContextDataMixin
from .models import Cart


class IndexItemList(ListView, ContextDataMixin):
    model = Item
    template_name = "index.html"
    context_object_name = 'items'
    extra_context = {
        'title': 'Главная страница',
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data() | super().get_context_for_nav()
        return context

    def get_queryset(self):
        return Item.publishes.get_index_objects()


class ItemListInCategory(ListView, ContextDataMixin):
    template_name = "products/item_list.html"
    context_object_name = 'items'

    def get_queryset(self):
        return Item.publishes.filter(category__slug=self.kwargs['category_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data() | super().get_context_for_nav()
        category = Category.publishes.filter(slug=self.kwargs['category_slug']).first()

        context |= {
            'title': category.name,
        }
        return context


class ItemDetail(DetailView, ContextDataMixin):
    model = Item
    template_name = 'products/new_item.html'
    context_object_name = 'item'
    slug_url_kwarg = 'item_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data() | super().get_context_for_nav()
        return context


class CategoryList(ListView, ContextDataMixin):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'category'
    slug_url_kwarg = 'category_slug'

    extra_context = {
        'title': 'Список категорий',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data() | super().get_context_for_nav()
        return context


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
