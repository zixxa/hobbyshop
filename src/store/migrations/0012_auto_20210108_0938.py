# Generated by Django 2.2 on 2021-01-08 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20210106_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.CharField(blank=True, max_length=255, verbose_name='URL'),
        ),
    ]
