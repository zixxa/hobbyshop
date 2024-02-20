# coding=utf-8
from django import template
from django.utils.safestring import mark_safe
from ..models import TemplateFragment, SiteLogo, SiteFavicon

register = template.Library()


@register.simple_tag()
def cms_template(name):
    """Вставка html-шаблонов из базы."""
    template = TemplateFragment.objects.get(name=name)
    return mark_safe(template.text)


@register.simple_tag()
def logo():
    """Вставка логотипа сайта."""
    try:
        logotype = SiteLogo.objects.first()
        if logotype is not None:
            return logotype.logo
        else:
            print("Not found logo!")
    finally:
        pass


@register.simple_tag()
def favicon():
    """Вставка фавикона сайта."""
    favicontype = SiteFavicon.objects.all()[0]
    return favicontype.favicon

