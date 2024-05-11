from django.contrib import admin
from .models import Appointment, Quote, VehicleShowing

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Quote)
admin.site.register(VehicleShowing)
