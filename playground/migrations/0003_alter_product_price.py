# Generated by Django 4.0.5 on 2022-07-09 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_remove_cartitems_cart_remove_cartitems_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
