from django.shortcuts import render
from src.store.models import Item, Type
from src.store.serializer import ItemSerializer
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response


class ItemView(APIView):
    queryset = Item.objects.filter(active_on=True).values()

    def get(self, request):
        items = Item.objects.filter(active_on=True)
        serializer = ItemSerializer(items, many=True)
        return Response({"items": serializer.data})


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
