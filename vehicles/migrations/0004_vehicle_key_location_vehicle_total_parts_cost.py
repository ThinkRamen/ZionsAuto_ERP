# Generated by Django 4.2.11 on 2024-04-29 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vehicles", "0003_vehicle_body_style_vehicle_drive_vehicle_photos"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehicle",
            name="key_location",
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name="vehicle",
            name="total_parts_cost",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
