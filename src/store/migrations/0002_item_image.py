# Generated by Django 2.2 on 2021-06-09 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to='image/', verbose_name='Изображение'),
        ),
    ]
