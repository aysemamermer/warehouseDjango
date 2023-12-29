from django.db import models

# Create your models here.
from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=255)
    inventory_number = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
