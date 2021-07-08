from django.contrib import admin

import os

from django.contrib.admin import ModelAdmin, register
from django.conf import settings
from .models import Item, Category

@register(Item)
class ItemAdmin(ModelAdmin):
    list_display = ('name', 'articel', 'slug', 'category',)

@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'parent', 'articel')

