# Generated by Django 3.1.5 on 2021-02-06 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210206_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_type',
        ),
    ]