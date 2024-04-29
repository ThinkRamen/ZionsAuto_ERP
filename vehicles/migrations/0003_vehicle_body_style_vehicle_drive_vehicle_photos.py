# Generated by Django 4.2.11 on 2024-04-29 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vehicles", "0002_vehicle_acquisition_cost"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehicle",
            name="body_style",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="vehicle",
            name="drive",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="vehicle",
            name="photos",
            field=models.ImageField(blank=True, null=True, upload_to="vehicle_photos"),
        ),
    ]
