from django.conf import settings
from django.shortcuts import render

# Create your views here.


def location(request):
    api_key = settings.MAPS_API_KEY
    return render(request, "location.html", {"api_key": api_key})
