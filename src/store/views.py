from django.shortcuts import render
from src.store.models import Item, Type
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    items = Item.objects.filter(active_on=True)
    types= Type.objects.all
    content = {'items':items,
               'types':types   
               }
    return render(request, 'index.html', content)

def item_page(request, item_slug):
    item = get_object_or_404(Item, slug=item_slug)
    item.save()

    content = {
        'item':item,
        'price':item.price
    }
    return render(request, 'products/new_item.html', content )
