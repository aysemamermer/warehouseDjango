# Generated by Django 5.0 on 2023-12-29 21:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Machine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("inventory_number", models.CharField(max_length=50, unique=True)),
                ("location", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
        ),
    ]