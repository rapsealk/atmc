from django.db import models


class Airline(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(max_length=3, unique=True, verbose_name="ICAO Airline Designator")
    name = models.CharField(max_length=32, unique=True)
    call_sign = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.code})"
