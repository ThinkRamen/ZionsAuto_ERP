from django.db import models
from locations.models import Location


class Vehicle(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    year = models.IntegerField(blank=True, null=True)
    make = models.CharField(max_length=100, blank=True, null=True)
    series = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    trim = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    body_style = models.CharField(max_length=50, blank=True, null=True)
    body_style = models.CharField(max_length=50, blank=True, null=True)
    key_location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        related_name="vehicles",
        null=True,
        blank=True,
    )
    drive = models.CharField(max_length=50, blank=True, null=True)
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    cylinder_count = models.IntegerField()
    engine_size = models.DecimalField(max_digits=4, decimal_places=2)
    acquisition_cost = models.DecimalField(max_digits=6, decimal_places=2)
    total_parts_cost = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )

    def __str__(self):
        return f"{self.year} {self.make} {self.model} {self.color} {self.vin}"  # Customize the representation

    def save(self, *args, **kwargs):
        # Check if the Vehicle instance has a primary key (i.e., has been saved to the database)
        if self.pk is None:
            super().save(*args, **kwargs)  # Save the Vehicle instance first

        # Calculate the total cost of all parts associated with this vehicle
        self.total_parts_cost = (
            sum(part.price for part in self.parts.all()) + self.acquisition_cost
        )
        super().save(*args, **kwargs)


class VehiclePhoto(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="vehicle_photos",
        null=True,
        blank=True,
    )
    image = models.ImageField(upload_to="vehicle_photos/")

    def __str__(self):
        return f"Vehicle Photo - {self.pk}"


class VehicleDocument(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="vehicle_documents",
        null=True,
        blank=True,
    )
    file = models.FileField(upload_to="document_files/")


class TodoItem(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    vehicle = models.ForeignKey(
        "Vehicle",
        on_delete=models.CASCADE,
        related_name="todo_items",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Vehicle Document - {self.pk}"
