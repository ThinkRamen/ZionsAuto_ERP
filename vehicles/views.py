from django.shortcuts import get_object_or_404, redirect, render

from .forms import VinForm
from .services import get_vin_decode
from .models import Vehicle
from django.conf import settings


# Create your views here.


def home(request):
    return render(request, "home.html")


def index(request):
    return render(request, "index.html")


def vehicles_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, "vehicles_list.html", {"vehicles": vehicles})


def vehicle_details(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)

    return render(request, "vehicle_details.html", {"vehicle": vehicle})


def add_vehicle_by_vin(request):
    form = VinForm
    return render(request, "admin/add-by-vin.html", {"form": form})
