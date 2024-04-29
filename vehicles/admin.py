from django.contrib import admin
from .models import Vehicle
from parts.models import Part


class PartInline(admin.TabularInline):
    model = Part
    extra = 0


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    inlines = [PartInline]
    list_display = ("make", "model", "year", "vin")
