from django.db import models


class Flight(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=16, null=False, unique=True)  # JNA121
    alias = models.CharField(max_length=16, null=True, unique=True)  # LJ121
    aircraft = models.ForeignKey("aircrafts.aircraft", related_name="flights", null=False, on_delete=models.CASCADE)
