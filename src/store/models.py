from django.db import models
from tinymce.models import HTMLField
from pytils.translit import slugify
import random

class Type(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural='Типы'

    def __str__(self):
        return self.name


class Item (models.Model):
    articel = models.IntegerField('Артикул', blank=True, null=True)
    title = models.CharField('Название', max_length = 255) 
    image = models.ImageField('Изображение', upload_to='image/', null=False)
    type = models.ForeignKey(Type, verbose_name='Тип', on_delete=models.CASCADE)
    slug = models.SlugField('URL', max_length = 255, blank=True) 
    description = HTMLField('Описание') 
    price = models.IntegerField(verbose_name='Цена', default=0, editable=True, blank=True, null=True)
    active_on=models.BooleanField("Активная", default='False', null='False')

    seo_title = models.CharField('SEO Название', max_length = 255, blank=True, null=True) 
    seo_description= models.CharField('SEO Описание', max_length = 255, blank=True, null=True) 

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural='Товары'

    def save(self, *args, **kwargs):
        if not self.articel:
            self.get_articel()
        super(Item,self).save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(self.title)
        super(Item,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_articel(self):
        id = random.randint(1000000, 9000000)
        if Item.objects.filter(articel=id):
            return self.get_articel()
        else:
            self.articel = id

