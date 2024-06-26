# Generated by Django 4.2.11 on 2024-04-29 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("locations", "0002_alter_location_address"),
        ("vehicles", "0004_vehicle_key_location_vehicle_total_parts_cost"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicle",
            name="key_location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="vehicles",
                to="locations.location",
            ),
        ),
    ]
