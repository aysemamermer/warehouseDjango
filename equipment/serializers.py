from rest_framework import serializers
from .models import Equipment, Machine


class EquipmentSerializer(serializers.ModelSerializer):
    machine_id = serializers.PrimaryKeyRelatedField(
        queryset=Machine.objects.all(), source='machine', required=False
    )

    class Meta:
        model = Equipment
        fields = ['id', 'name', 'inventory_number', 'machine_id', 'created_at']

    def create(self, validated_data):
        machine_id = validated_data.pop('machine_id', None)
        equipment = super().create(validated_data)
        if machine_id:
            equipment.machine_id = machine_id
        equipment.save()

        self.add_success_message(equipment, created=True)
        return equipment

    def update(self, instance, validated_data):
        instance.__dict__.update(validated_data)
        instance.save()

        if Equipment.objects.exclude(id=instance.id).filter(
                inventory_number=validated_data['inventory_number']).exists():
            raise serializers.ValidationError("Inventory number already exists.")

        self.add_success_message(instance, created=False)
        return instance

    def add_success_message(self ,instance , created):
        success_message = "Equipment created successfully!" if created else "Equipment updated successfully!"
        setattr(self.context['view'], 'success_message', success_message)
