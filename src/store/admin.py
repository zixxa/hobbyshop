from django.contrib import admin

import os

from django.contrib.admin import ModelAdmin, register
from django.conf import settings
from .models import Item, Type 

@register(Item)
class ItemAdmin(ModelAdmin):
    list_display = ('title', 'slug', 'type')


@register(Type)
class TypeAdmin(ModelAdmin):
    list_display = ('name',)
