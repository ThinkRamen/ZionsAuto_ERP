from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="children", null=True, blank=True
    )

    def __str__(self):
        return f"{self.name}"
