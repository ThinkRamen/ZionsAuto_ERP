from django.contrib import admin
from .models import Vehicle
from parts.models import Part
from .models import VehiclePhoto, VehicleDocument, TodoItem


class PartInline(admin.TabularInline):
    model = Part
    extra = 0


class VehiclePhotoInline(admin.TabularInline):
    model = VehiclePhoto
    extra = 1


class VehicleDocumentInline(admin.TabularInline):
    model = VehicleDocument
    extra = 1


class TodoInline(admin.TabularInline):
    model = TodoItem
    extra = 1


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    inlines = [PartInline, VehiclePhotoInline, VehicleDocumentInline, TodoInline]
    list_display = ("make", "model", "year", "vin")
