from django.db import models
from vehicles.models import Vehicle, VehiclePhoto


class FacebookAd(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photos = models.ForeignKey(
        VehiclePhoto, on_delete=models.CASCADE, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # Override the save method to update the title based on the associated Vehicle properties
    def save(self, *args, **kwargs):
        # Construct the title from the vehicle properties
        self.title = f"{self.vehicle.year} {self.vehicle.make} {self.vehicle.model} {self.vehicle.color}"
        super().save(*args, **kwargs)

    def __str__(self):
        if hasattr(self, "title"):  # Check if the title attribute exists
            return self.title
        else:
            return super().__str__()  # Fallback to default string representation


from django.db import models
from vehicles.models import Vehicle, VehiclePhoto


class OfferUpAd(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photos = models.ForeignKey(
        VehiclePhoto, on_delete=models.CASCADE, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # Override the save method to update the title based on the associated Vehicle properties
    def save(self, *args, **kwargs):
        # Construct the title from the vehicle properties
        self.title = f"{self.vehicle.year} {self.vehicle.make} {self.vehicle.model} {self.vehicle.color}"
        super().save(*args, **kwargs)

    def __str__(self):
        if hasattr(self, "title"):  # Check if the title attribute exists
            return self.title
        else:
            return super().__str__()  # Fallback to default string representation
