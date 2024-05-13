from django.urls import path
from . import views

app_name = "appointments"

urlpatterns = [
    path("create-showing/", views.app_vehicle_showing, name="create-showing"),
    path("create-quote/", views.app_quote, name="create-quote"),
    path("create-appointment/", views.create_appointment, name="create-appointment"),
]
