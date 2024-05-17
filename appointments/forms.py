from django import forms
from .models import Appointment, Quote, VehicleShowing


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["first_name", "last_name", "date", "time"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
        }


class VehicleShowingForm(forms.ModelForm):
    class Meta:
        model = VehicleShowing
        fields = ["first_name", "last_name", "date", "time", "vehicle"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
        }


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["first_name", "last_name", "date", "time", "description"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
        }
