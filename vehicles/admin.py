from django.contrib import messages
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from vehicles.forms import VinForm
from .models import Vehicle
from parts.models import Part
from django.template.response import TemplateResponse
from .models import VehiclePhoto, VehicleDocument, TodoItem
from semantic_admin import (
    SemanticModelAdmin,
    SemanticStackedInline,
    SemanticTabularInline,
)
from django.contrib.auth.admin import UserAdmin


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
    change_list_template = "admin/model_change_list.html"
    inlines = [PartInline, VehiclePhotoInline, VehicleDocumentInline, TodoInline]
    list_display = ("make", "model", "year", "vin")

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                "add-by-vin/",
                self.admin_site.admin_view(self.add_by_vin),
                name="add_by_vin",
            ),
        ]
        return my_urls + urls

    def add_by_vin(self, request):
        if request.method == "POST":
            form = VinForm(request.POST)
            if form.is_valid():
                vehicle = form.save()
                messages.success(request, "Vehicle successfully added.")
                return HttpResponseRedirect(
                    reverse("admin:vehicles_vehicle_change", args=[vehicle.pk])
                )
        else:
            form = VinForm()

        context = {
            **self.admin_site.each_context(request),
            "form": form,
        }
        return TemplateResponse(request, "admin/add-by-vin.html", context)
