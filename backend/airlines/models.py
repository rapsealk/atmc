from django.db import models


class Airline(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(max_length=3, unique=True, verbose_name="ICAO Airline Code")
    # iata = models.CharField(max_length=2, unique=True, verbose_name="IATA Airline Designator")
    name = models.CharField(max_length=32, unique=True)
    call_sign = models.CharField(max_length=16)
