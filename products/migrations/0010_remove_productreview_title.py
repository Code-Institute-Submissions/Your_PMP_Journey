# Generated by Django 3.1.5 on 2021-02-20 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_productreview_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productreview',
            name='title',
        ),
    ]
