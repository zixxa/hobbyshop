# Generated by Django 3.1 on 2020-10-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/', verbose_name='Изображение'),
        ),
    ]
