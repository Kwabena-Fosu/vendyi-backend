# Generated by Django 4.2.5 on 2023-09-26 15:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=500)),
                ('location', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=50)),
                ('website', models.URLField(validators=[django.core.validators.URLValidator()])),
                ('ID_card', models.ImageField(blank=True, null=True, upload_to='media/vendors/ID_cards', validators=[django.core.validators.validate_image_file_extension])),
                ('is_active', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
            options={
                'verbose_name': 'Vendor',
                'verbose_name_plural': 'Vendors',
            },
            managers=[
                ('active_vendors', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='VendorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='media/profile.jpeg', upload_to='media/vendors/profiles', validators=[django.core.validators.validate_image_file_extension])),
                ('header_image', models.ImageField(upload_to='media/vendors/headers', validators=[django.core.validators.validate_image_file_extension])),
                ('followers', models.ManyToManyField(default='media/profile.jpeg', related_name='following', to='account.user')),
                ('vendor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor')),
            ],
        ),
    ]
