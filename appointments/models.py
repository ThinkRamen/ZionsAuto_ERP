from django.db import models
from django.core.exceptions import ValidationError
import re
from vehicles.models import Vehicle


def validate_phone_number(value):
    """
    Custom validator for USA phone numbers.
    Validates that the value is a valid USA phone number format.
    """
    # Regular expression pattern for typical USA phone number formats
    phone_number_pattern = r"^\+?1?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"

    if not re.match(phone_number_pattern, value):
        raise ValidationError("Please enter a valid phone number.")


class Appointment(models.Model):
    date_time = models.DateTimeField()
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    phone_number = models.CharField(
        max_length=20, blank=True, validators=[validate_phone_number]
    )

    def __str__(self):
        return f"Appointment at {self.date_time} - {self.first_name} {self.last_name}"


class Quote(Appointment):
    description = models.TextField()


class VehicleShowing(Appointment):
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE
    )  # ForeignKey to the Vehicle model

    def __str__(self):
        return f"Vehicle showing for {self.vehicle} at {self.date_time} - {self.first_name} {self.last_name}"
