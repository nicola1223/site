# Generated by Django 5.1.4 on 2025-01-20 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0004_rename_truck_image_truck_truck_main_image_truckimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='truck_main_image',
            field=models.ImageField(blank=True, null=True, upload_to='truck_photos'),
        ),
    ]
