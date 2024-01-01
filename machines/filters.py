# filters.py
import django_filters
from .models import Machine

class MachineFilter(django_filters.FilterSet):
    class Meta:
        model = Machine
        fields = {
            'name': ['exact', 'icontains'],
            'inventory_number': ['exact', 'icontains'],
            'location': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
        }
