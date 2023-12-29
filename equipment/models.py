
# Create your models here.
from django.db import models
from machines.models import Machine

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    inventory_number = models.CharField(max_length=50, unique=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
