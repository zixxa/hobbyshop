from django.db import models
from pytils.translit import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from mptt.models import MPTTModel, TreeForeignKey
from .managers import ActiveObjectsManager


class Category(MPTTModel):
    articel = models.CharField('Название', max_length=3, default="000")
    name = models.CharField('Название', max_length=255)
    icon = models.ImageField('Иконка (для главных категорий)', upload_to='images/icons', null=True, blank=True)
    image = models.ImageField('Изображение', upload_to='images/', null=True, blank=True)
    slug = models.SlugField('URL', max_length=255, blank=True)
    parent = TreeForeignKey('self', verbose_name='Родительская категория', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')
    active_on = models.BooleanField('Активная', default=False, null=False)

    is_show_on_index = models.BooleanField('Показывать на главной', default=False, null=False)

    objects = models.Manager()
    publishes = ActiveObjectsManager()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def save(self, *args, **kwargs):
        if not self.articel and self.pk:
            self.articel = '0' * (3 - len(str(self.id))) + str(self.id)
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Item(models.Model):
    articel = models.CharField('Артикул товара', max_length=3, blank=True, null=True, default="000")
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField('URL', max_length=255, blank=True)
    image = models.ImageField('Изображение', upload_to='images/', null=True)
    description = HTMLField('Описание')
    price = models.IntegerField(verbose_name='Цена', default=0, editable=True, blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, null=True, blank=True)

    active_on = models.BooleanField('Активная', default=False, null=False)
    is_show_on_index = models.BooleanField('Показывать на главной странице', default=False, null=False)

    seo_title = models.CharField('SEO Название', max_length=255, blank=True, null=True)
    seo_description = models.CharField('SEO Описание', max_length=255, blank=True, null=True)

    objects = models.Manager()
    publishes = ActiveObjectsManager()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def save(self, *args, **kwargs):
        if not self.articel and self.pk:
            self.articel = '0' * (3 - len(str(self.pk))) + str(self.pk)
        if not self.slug:
            self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('content_item', kwargs={'item_slug': self.slug})


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    quanity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quanity} x {self.product}"

    def get_absolute_url(self):
        return reverse("cart:cart_detail")
