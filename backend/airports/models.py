from django.db import models


class Airport(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(max_length=4, unique=True, verbose_name="ICAO Airport Code")
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.code})"
