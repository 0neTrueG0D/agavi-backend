# Generated by Django 5.0 on 2024-10-02 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0001_initial"),
        ("products", "0008_product_average_rating_value"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="cartitem",
            unique_together={("cart", "product")},
        ),
    ]
