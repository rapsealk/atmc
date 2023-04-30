from django.db import models
from django.utils.translation import gettext_lazy as _


class Flight(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=16, null=False, unique=True)  # JNA121
    alias = models.CharField(max_length=16, null=True, unique=True)  # LJ121
    aircraft = models.ForeignKey(
        "aircrafts.aircraft",
        related_name="flights",
        null=False,
        on_delete=models.CASCADE,
    )
    origin = models.ForeignKey(
        "airports.airport",
        related_name="departures",
        null=False,
        on_delete=models.CASCADE,
    )  # departure
    destination = models.ForeignKey(
        "airports.airport",
        related_name="arrivals",
        null=False,
        on_delete=models.CASCADE,
    )  # arraival
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class FlightSchedule(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", _("PENDING")
        PREFLIGHT = "PREFLIGHT", _("PREFLIGHT")

    id = models.UUIDField(primary_key=True)
    flight = models.ForeignKey("flights.flight", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=Status.choices)
