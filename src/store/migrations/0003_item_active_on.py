# Generated by Django 2.2 on 2020-11-02 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20201013_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='active_on',
            field=models.BooleanField(default='False', null='False', verbose_name='Активная'),
            preserve_default='False',
        ),
    ]
