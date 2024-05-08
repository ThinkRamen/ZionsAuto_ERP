from django.shortcuts import render
from .models import Vehicle

# Create your views here.


def home(request):
    vehicles = Vehicle.objects.all()
    return render(request, "home.html", {"vehicles": vehicles})
