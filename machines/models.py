from django.db import models


class Machine(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=255)
    inventory_number = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def formatted_created_at(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return self.name
