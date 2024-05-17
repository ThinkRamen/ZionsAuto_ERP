from django.shortcuts import render
from .models import Vehicle
from django.conf import settings


# Create your views here.


def home(request):
    return render(request, "home.html")


def location(request):
    api_key = settings.MAPS_API_KEY
    return render(request, "location.html", {"api_key": api_key})


def vehicles_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, "vehicles/vehicles_list.html", {"vehicles": vehicles})
