from django.db import models


class Aircraft(models.Model):
    id = models.UUIDField(primary_key=True)
    type = models.CharField(max_length=8)  # enum (B738)
    airline = models.ForeignKey("airlines.airline", related_name="aircrafts", on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=16)  # Boeing, Airbus
