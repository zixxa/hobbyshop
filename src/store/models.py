from django.db import models
from tinymce.models import HTMLField
from pytils.translit import slugify
from mptt.models import MPTTModel, TreeForeignKey


class Articel(models.Model):
    code = models.CharField('Код', max_length=255, blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = 'Артикул'
        verbose_name_plural = 'Артикулы'

    def __str__(self):
        return self.code

class ArticelCategory(Articel):
    parent = TreeForeignKey('self', verbose_name='Артикул категорий', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='articel_children')

class ArticelItem(Articel):
    category = models.ForeignKey(ArticelCategory, verbose_name='Артикул', on_delete=models.CASCADE, null=True, blank=True)


class Category(MPTTModel):
    articel = models.OneToOneField(ArticelCategory, verbose_name='Артикул', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField('Название', max_length=255)
    icon = models.ImageField('Иконка (для главных категорий)', upload_to='images/icons', null=True, blank=True)
    image = models.ImageField('Изображение', upload_to='images/', null=True, blank=True)
    slug = models.SlugField('URL', max_length = 255, blank=True)
    parent = TreeForeignKey('self', verbose_name='Родительская категория', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def save(self, *args, **kwargs):
        code = '0' * (3 - len(str(self.id))) + str(self.id)
        try:
            parent = ArticelCategory.objects.get(id=self.parent.articel.id) if self.parent.articel else None
        except:
            parent = None
        articel = ArticelCategory.objects.create(code=code, parent=parent)
        print(code)
        self.articel = articel
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Item (models.Model):
    articel = models.OneToOneField(ArticelItem, verbose_name='Артикул', on_delete=models.CASCADE, null=True, blank=True)
    full_articel = models.CharField('Артикул товара', max_length = 255, blank=True, null=True)
    name = models.CharField('Название', max_length = 255)
    slug = models.SlugField('URL', max_length = 255, blank=True)
    image = models.ImageField('Изображение', upload_to='images/', null=True)
    description = HTMLField('Описание')
    price = models.IntegerField(verbose_name='Цена', default=0, editable=True, blank=True, null=True)
    active_on = models.BooleanField('Активная', default='False', null='False')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, null=True, blank=True)

    seo_title = models.CharField('SEO Название', max_length = 255, blank=True, null=True)
    seo_description = models.CharField('SEO Описание', max_length = 255, blank=True, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural='Товары'

    def save(self, *args, **kwargs):
        self.make_articel()
        if not self.slug:
            self.slug = slugify(self.name)
        super(Item,self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def make_articel(self):
        if not self.category.articel:
            code = '0' * (3 - len(str(self.category.id))) + str(self.category.id)
            ArticelCategory.objects.create(code=code, parent=(self.category.parent.articel.id if self.category.parent.articel else None))
        code = '0' * (3 - len(str(self.id))) + str(self.id)
        category = ArticelCategory.objects.get(id=self.category.articel.id) if self.category.articel else None
        articel = ArticelItem.objects.create(code = code, category = category)
        self.articel = articel
        if self.category:
            categories = "".join([i.articel.code for i in self.category.get_ancestors(include_self=True)])
        else:
            categories = ""
        self.full_articel = categories + self.articel.code
        return self.full_articel

