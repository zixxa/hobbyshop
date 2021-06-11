# Generated by Django 2.2 on 2021-06-10 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='type',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='URL'),
        ),
    ]
