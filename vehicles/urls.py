from django.urls import path
from . import views

urlpatterns = [
    path("", views.vehicles_list, name="vehicles"),
    path("vehicle/<pk>", views.vehicle_details, name="vehicle-details"),
    path("admin/vehicles/add-by-vin", views.add_vehicle_by_vin, name="add-by-vin"),
]
