from django.db import models
from vehicles.models import Vehicle
from locations.models import Location
import uuid
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
from django.urls import reverse


class Part(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    part_number = models.CharField(max_length=50, unique=True)
    part_location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="part_locations",
        null=True,
        blank=True,
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE, related_name="parts", null=True, blank=True
    )
    barcode = models.CharField(max_length=8, blank=True, null=True)
    qr_code = models.ImageField(upload_to="qr_codes", blank=True, null=True)
    serial_number = models.CharField(max_length=6, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.part_number} - {self.vehicle}"  # Customize the representation

    def save(self, *args, **kwargs):
        if not self.serial_number:
            self.serial_number = (
                uuid.uuid4().hex[:6].upper()
            )  # Generate unique serial number
        if not self.barcode:
            self.barcode = uuid.uuid4().hex[:8].upper()  # Generate unique barcode

        # Generate URL for the part's admin view
        part_url = reverse("admin:parts_part_change", args=[self.pk])

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f"http://127.0.0.1:8000{part_url}")
        qr.make(fit=True)

        # Create PIL image
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        filename = f"{self.name}_{uuid.uuid4().hex[:8]}.png"  # Using a portion of UUID as a unique identifier

        # Save image to the model field
        self.qr_code.save(filename, File(buffer), save=False)

        super().save(*args, **kwargs)
