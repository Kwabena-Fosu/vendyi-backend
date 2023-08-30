# Generated by Django 4.2 on 2023-08-29 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_coloroption_sizeoption_remove_product_size_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="discount_end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="discount_percentage",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="discount_start_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
