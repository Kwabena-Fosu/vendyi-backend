# Generated by Django 4.2.5 on 2023-09-26 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_userprofile_image'),
        ('vendors', '0005_alter_vendorprofile_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to='account.user'),
        ),
    ]
