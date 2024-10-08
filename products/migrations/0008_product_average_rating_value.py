# Generated by Django 5.0 on 2024-09-29 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0007_remove_product_image_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="average_rating_value",
            field=models.DecimalField(
                decimal_places=1, default=0.0, editable=False, max_digits=2
            ),
        ),
    ]
