# Generated by Django 5.0.1 on 2024-03-03 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_item_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='active_on',
            field=models.BooleanField(default=False, verbose_name='Активная'),
        ),
        migrations.AlterField(
            model_name='item',
            name='active_on',
            field=models.BooleanField(default=False, verbose_name='Активная'),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_show_on_index',
            field=models.BooleanField(default=False, verbose_name='Показывать на главной странице'),
        ),
    ]