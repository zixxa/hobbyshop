from robokassa.forms import RobokassaForm
from src.store.models import Item, Category
from src.store.serializer import ItemSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from cart.cart import Cart


class ItemViewSet(ViewSet):

    def list(self, request):
        items = Item.objects.filter(active_on=True)
        serializer = ItemSerializer(items, many=True)
        return Response({"items": serializer.data})


def index(request):
    items = Item.objects.filter(active_on=True)
    categories = Category.objects.all
    content = {
            'items':items,
            'categories':categories
    }
    return render(request, 'index.html', content)


def item_page(request, item_slug):
    item = get_object_or_404(Item, slug=item_slug)
    categories = Category.objects.all

    content = {
        'item':item,
        'categories':categories,
        'price':item.price
    }
    return render(request, 'products/new_item.html', content)


def category_list(request, parent_slug):
    parent = get_object_or_404(Category, slug=parent_slug)
    categories = Category.objects.all
    subcategories = Category.objects.filter(parent=parent)

    content = {
        'categories':categories,
        'subcategories':subcategories,
    }
    return render(request, 'products/category_list.html', content)


def item_list(request, parent_slug, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    items = Item.objects.filter(category=category)
    categories = Category.objects.all

    content = {
        'categories':categories,
        'items':items,
    }
    return render(request, 'products/item_list.html', content)

''' Управление корзиной '''

@login_required(login_url="/users/signin")
def cart_add(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.add(product=product)
    return redirect("/")


@login_required(login_url="/users/signin")
def item_clear(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/signin")
def item_increment(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/signin")
def item_decrement(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/signin")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/signin")
def cart_detail(request):
    categories = Category.objects.all

    content = {
        'categories':categories,
    }
    return render(request, 'products/cart_detail.html', content)

@login_required
def pay_with_robokassa(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    form = RobokassaForm(initial={
               'OutSum': order.total,
               'InvId': order.id,
               'Desc': order.name,
               'Email': request.user.email,
               # 'IncCurrLabel': '',
               # 'Culture': 'ru'
           })

    return render(request, 'pay_with_robokassa.html', {'form': form})