from rest_framework import serializers
from .models import Equipment, Machine


class EquipmentSerializer(serializers.ModelSerializer):
    """Define a PrimaryKeyRelatedField for the machine_id to allow setting the machine when creating or updating"""
    machine_id = serializers.PrimaryKeyRelatedField(
        queryset=Machine.objects.all(), source='machine', required=False
    )

    class Meta:
        model = Equipment
        fields = ['id', 'name', 'inventory_number', 'machine_id', 'created_at']

    def create(self, validated_data):
        """Extract machine_id if provided and pop it from validated_data"""
        machine_id = validated_data.pop('machine_id', None)
        equipment = super().create(validated_data)
        # Set the machine_id for the equipment if provided
        if machine_id:
            equipment.machine_id = machine_id
        equipment.save()

        """Add success message to the view"""
        self.add_success_message(equipment, created=True)
        return equipment

    def update(self, instance, validated_data):
        instance.__dict__.update(validated_data)
        instance.save()

        """Check for duplicate inventory_number"""
        if Equipment.objects.exclude(id=instance.id).filter(
                inventory_number=validated_data['inventory_number']).exists():
            raise serializers.ValidationError("Inventory number already exists.")

        """Add success message to the view"""
        self.add_success_message(instance, created=False)
        return instance

    def add_success_message(self, instance, created):
        """Add success message to the view's context """
        success_message = "Equipment created successfully!" if created else "Equipment updated successfully!"
        setattr(self.context['view'], 'success_message', success_message)
