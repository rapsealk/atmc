from django.db import models


class Airport(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(max_length=4, unique=True, verbose_name="ICAO Airport Code")
    iata = models.CharField(max_length=3, unique=True, verbose_name="IATA Airport Code")
    name = models.CharField(max_length=64)
