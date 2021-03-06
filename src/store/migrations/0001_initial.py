# Generated by Django 3.1 on 2020-10-13 06:58

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articel', models.IntegerField(default=0, verbose_name='Артикул')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='item_image', verbose_name='Изображение')),
                ('slug', tinymce.models.HTMLField(verbose_name='Описание')),
                ('price', models.IntegerField(default=0, null=True, verbose_name='Цена')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.type', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
