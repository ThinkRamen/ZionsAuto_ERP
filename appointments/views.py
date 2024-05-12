from django.shortcuts import render
from .models import Appointment

# Create your views here.


def AppointmentView(request):
    return render(
        request, "appointments/create_appointment.html", {"appointment": Appointment}
    )
