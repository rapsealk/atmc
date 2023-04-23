from django.db import models


class Airline(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
