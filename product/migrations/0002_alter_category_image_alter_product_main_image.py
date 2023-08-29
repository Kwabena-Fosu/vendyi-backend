# Generated by Django 4.2 on 2023-08-29 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="media/category/"),
        ),
        migrations.AlterField(
            model_name="product",
            name="main_image",
            field=models.ImageField(upload_to="media/products/"),
        ),
    ]
