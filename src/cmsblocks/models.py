from django.db import models

class TemplateFragment(models.Model):
    """html-шаблон для вставки на сайт."""
    name = models.CharField('Название шаблона', max_length=25, db_index=True)
    description = models.CharField('Описание шаблона', max_length=255, blank=True)
    text = models.TextField('Текст шаблона', blank=True, default='')

    class Meta:
        verbose_name = 'Файл шаблона'
        verbose_name_plural = 'Файлы шаблона'


class SiteLogo(models.Model):
    """Логотип сайта."""
    logo = models.ImageField('Логотип', upload_to='logo', blank=False, null=False)

    class Meta:
        verbose_name = 'Логотип сайта'
        verbose_name_plural = 'Логотипы сайта'


class SiteFavicon(models.Model):
    """Фавикон сайта."""
    favicon = models.ImageField('Фавикон', upload_to='favicon', blank=False, null=False)

    class Meta:
        verbose_name = 'Фавикон сайта'
        verbose_name_plural = 'Фавиконы сайта'


