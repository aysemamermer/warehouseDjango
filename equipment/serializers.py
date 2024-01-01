from rest_framework import serializers
from .models import Equipment, Machine

class EquipmentSerializer(serializers.ModelSerializer):
    machine_id = serializers.PrimaryKeyRelatedField(
        queryset=Machine.objects.all(), source='machine', required=False
    )

    class Meta:
        model = Equipment
        fields = ['id', 'name', 'inventory_number', 'machine_id', 'created_at']

    def validate_inventory_number(self, value):
        if self.instance and self.instance.inventory_number == value:
            return value

        if Equipment.objects.filter(inventory_number=value).exists():
            raise serializers.ValidationError("Another equipment with this inventory number already exists.")

        return value

    def create(self, validated_data):
        machine_id = validated_data.pop('machine_id', None)
        equipment = super().create(validated_data)
        if machine_id:
            equipment.machine_id = machine_id
            equipment.save()
        return equipment

    def update(self, instance, validated_data):
        machine_id = validated_data.pop('machine_id', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if machine_id:
            instance.machine_id = machine_id

        instance.save()
        self.add_success_message(instance, created=False)
        return instance

    def add_success_message(self, instance, created):
        success_message = "Equipment created successfully!" if created else "Equipment updated successfully!"
        setattr(self.context['view'], 'success_message', success_message)
