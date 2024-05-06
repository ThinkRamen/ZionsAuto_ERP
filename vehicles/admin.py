from django.contrib import admin
from .models import Vehicle
from parts.models import Part
from .models import VehiclePhoto, VehicleDocument, TodoItem
from semantic_admin import (
    SemanticModelAdmin,
    SemanticStackedInline,
    SemanticTabularInline,
)


class PartInline(SemanticStackedInline):
    model = Part
    extra = 0


class VehiclePhotoInline(SemanticTabularInline):
    model = VehiclePhoto
    extra = 1


class VehicleDocumentInline(SemanticTabularInline):
    model = VehicleDocument
    extra = 1


class TodoInline(SemanticTabularInline):
    model = TodoItem
    extra = 1


@admin.register(Vehicle)
class VehicleAdmin(SemanticModelAdmin):
    inlines = [PartInline, VehiclePhotoInline, VehicleDocumentInline, TodoInline]
    list_display = ("make", "model", "year", "vin")
