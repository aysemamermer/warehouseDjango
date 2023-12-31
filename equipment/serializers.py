from rest_framework import serializers
from .models import Equipment, Machine

class EquipmentSerializer(serializers.ModelSerializer):
    machine_id = serializers.PrimaryKeyRelatedField(
        queryset=Machine.objects.all(), source='machine', required=False
    )

    class Meta:
        model = Equipment
        fields = ['id', 'name', 'inventory_number', 'machine_id', 'created_at']

    # ...

    def create(self, validated_data):
        machine_id = validated_data.pop('machine_id', None)
        equipment = super().create(validated_data)
        if machine_id:
            equipment.machine_id = machine_id
            equipment.save()
        return equipment

    def update(self, instance, validated_data):
        machine_id = validated_data.pop('machine_id', None)
        instance = super().update(instance, validated_data)
        if machine_id:
            instance.machine_id = machine_id
            instance.save()
        return instance
