# Generated by Django 3.0.6 on 2020-05-10 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_products_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='product_name',
            new_name='rest_name',
        ),
    ]