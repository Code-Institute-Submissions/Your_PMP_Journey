# Generated by Django 3.1.5 on 2021-02-05 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_book_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='book_type',
            field=models.CharField(choices=[('HD', 'Hardback'), ('KI', 'Kindle'), ('PB', 'Paperback'), ('NO', 'None')], default='NO', max_length=2),
        ),
    ]
