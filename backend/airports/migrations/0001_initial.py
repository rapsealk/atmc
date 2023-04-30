# Generated by Django 4.2 on 2023-04-30 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Airport",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                (
                    "code",
                    models.CharField(
                        max_length=4, unique=True, verbose_name="ICAO Airport Code"
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_modified_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
