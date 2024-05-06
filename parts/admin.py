from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from .models import Part
from semantic_admin import SemanticModelAdmin
from django.db import models


class PartAdmin(SemanticModelAdmin):
    fields = [
        "name",
        "manufacturer",
        "part_number",
        "part_location",
        "description",
        "price",
        "vehicle",
        "photos",
        "receipts",
        "barcode",
        "qr_code_preview",
    ]
    readonly_fields = ["qr_code_preview"]

    def qr_code_preview(self, obj):
        if obj.qr_code:
            return mark_safe(
                f"<a href=\"#\" onclick=\"window.open('{obj.qr_code.url}', '_blank');\">"
                f'<img src="{obj.qr_code.url}" alt="QR Code Preview" class="ui centered image"/>'
                f"</a><"
            )
        return "-"

    qr_code_preview.short_description = "QR Code Preview"
    qr_code_preview.allow_tags = True


admin.site.register(Part, PartAdmin)
