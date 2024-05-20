from pyexpat.errors import messages
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from .models import Vehicle
from .services import get_vin_decode


class VinForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            "vin",
        ]  # Add other fields if needed

    def save(self, commit=True):
        # Create a new Vehicle instance
        vehicle = super().save(commit=False)

        # Fetch additional information using get_vin_decode()
        vin_info = get_vin_decode(vehicle.vin)
        print(vin_info)

        # Assign additional attributes based on the fetched information
        if vin_info:
            vehicle.year = vin_info.get("Model Year")
            vehicle.make = vin_info.get("Make")
            vehicle.model = vin_info.get("Model")
            vehicle.series = vin_info.get("Series")
            vehicle.trim = vin_info.get("Trim")
            vehicle.body_style = vin_info.get("Body Style")
            vehicle.doors = vin_info.get("Doors")
            vehicle.fuel_type = vin_info.get("Fuel Type - Primary")
            vehicle.cylinder_count = vin_info.get("Engine Number of Cylinders")
            vehicle.engine_size = vin_info.get("Displacement (L)")

        if commit:
            try:
                vehicle.save()
            except forms.ValidationError as e:
                # Iterate through errors and display them as messages
                for field, errors in e.message_dict.items():
                    for error in errors:
                        messages.error(self.request, f"Error in {field}: {error}")
                # Reraise the exception to propagate it
                raise e

        return vehicle
