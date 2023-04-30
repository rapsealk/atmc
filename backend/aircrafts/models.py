from django.db import models
from django.utils.translation import gettext_lazy as _


class Aircraft(models.Model):
    class Manufacturer(models.TextChoices):
        AIRBUS = "A", _("Airbus")
        BOEING = "B", _("Boeing")

    id = models.UUIDField(primary_key=True)
    type = models.CharField(max_length=8)  # enum (B738)
    airline = models.ForeignKey(
        "airlines.airline", related_name="aircrafts", on_delete=models.CASCADE
    )
    manufacturer = models.CharField(max_length=1, choices=Manufacturer.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return f"{self.type} ({self.id})"
