# Generated by Django 2.2 on 2021-06-02 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20210517_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='level',
        ),
        migrations.RemoveField(
            model_name='type',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='type',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='type',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='type',
            name='tree_id',
        ),
    ]