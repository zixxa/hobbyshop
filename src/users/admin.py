from django.contrib import admin

import os

from django.contrib.admin import ModelAdmin, register
from django.conf import settings
from src.users.models import Profile

@register(Profile)
class ItemAdmin(ModelAdmin):
    list_display = ('user',)

