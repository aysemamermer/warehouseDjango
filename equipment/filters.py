# filters.py
import django_filters
from .models import Equipment

class EquipmentFilter(django_filters.FilterSet):
    class Meta:
        model = Equipment
        fields = {
            'name': ['exact', 'icontains'],
            'inventory_number': ['exact', 'icontains'],
        }
