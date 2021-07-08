from django.db import models
from tinymce.models import HTMLField
from pytils.translit import slugify
from mptt.models import MPTTModel, TreeForeignKey
import random

#class Articel(models.Model):
#    category_part = models.ForeignKey()

class Category(MPTTModel):
    articel = models.CharField('Артикул категории', max_length = 255, blank=True, null=True)
    name = models.CharField('Название', max_length=255)
    icon = models.ImageField('Иконка (для главных категорий)', upload_to='images/icons', null=True, blank=True)
    image = models.ImageField('Изображение', upload_to='images/', null=True, blank=True)
    slug = models.SlugField('URL', max_length = 255, blank=True)
    parent = TreeForeignKey('self', verbose_name='Родительская категория', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural='Категории'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Item (models.Model):
    articel = models.CharField('Артикул', max_length = 255, blank=True, null=True)
    name = models.CharField('Название', max_length = 255)
    slug = models.SlugField('URL', max_length = 255, blank=True)
    image = models.ImageField('Изображение', upload_to='images/', null=True)
    description = HTMLField('Описание')
    price = models.IntegerField(verbose_name='Цена', default=0, editable=True, blank=True, null=True)
    active_on = models.BooleanField('Активная', default='False', null='False')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, null=True, blank=True)

    seo_title = models.CharField('SEO Название', max_length = 255, blank=True, null=True)
    seo_description= models.CharField('SEO Описание', max_length = 255, blank=True, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural='Товары'

    def save(self, *args, **kwargs):
        if not self.articel:
            self.make_articel()
        if not self.slug:
            self.slug = slugify(self.name)
        super(Item,self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def make_articel(self):
        items = len(Item.objects.filter(category=self.category)) - len()
        id = self.category.articel + str(len(Item.objects.filter(category=self.category)) + 1)
        #if Item.objects.filter(articel=id):
        #    return self.make_articel()
        self.articel = id
        return self.articel

