from django.shortcuts import render
from .models import Vehicle

# Create your views here.


def home(request):
    return render(request, "home.html")


def vehicles_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, "vehicles/vehicles_list.html", {"vehicles": vehicles})
