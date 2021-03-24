# coding=utf-8
from django.contrib import admin
from django.db import models
from django.forms import Textarea
from .models import TemplateFragment, SiteLogo, SiteFavicon


@admin.register(TemplateFragment)
class TemplateFragmentAdmin(admin.ModelAdmin):
    """Админка для фрагментов шаблонов."""
    list_display = ['name', 'description']
    icon_name = 'camera'
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 30, 'cols': 150})},
    }


@admin.register(SiteLogo)
class LogoAdmin(admin.ModelAdmin):
    """Админка для логотипов сайта."""
    list_display = ['id', 'logo']
    icon_name = 'blur_on'


@admin.register(SiteFavicon)
class FaviconAdmin(admin.ModelAdmin):
    """Админка для фавиконов сайта."""
    list_display = ['id', 'favicon']
    icon_name = 'blur_on'

