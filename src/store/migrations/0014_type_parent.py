# Generated by Django 2.2 on 2021-05-17 11:49

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20210108_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='types', to='store.Type'),
        ),
    ]