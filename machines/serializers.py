# serializers.py

from .models import Machine
from rest_framework import serializers

class MachineSerializer(serializers.ModelSerializer):
    """
    Serializer for the Machine model.
    """

    class Meta:
        model = Machine
        fields = ['id', 'name', 'inventory_number', 'location', 'description', 'created_at']

    def create(self, validated_data):
        """
        Override the create method to include a success message upon successful creation.
        """
        instance = super().create(validated_data)
        self.add_success_message(instance, created=True)
        return instance

    def update(self, instance, validated_data):
        """
        Override the update method to include a success message upon successful update.
        """
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        if Machine.objects.exclude(id=instance.id).filter(inventory_number=validated_data['inventory_number']).exists():
            raise serializers.ValidationError("Inventory number already exists.")

        self.add_success_message(instance, created=False)
        return instance

    def add_success_message(self, instance, created):
        """
        Helper method to add a success message to the view upon successful creation or update.
        """
        success_message = "Machine created successfully!" if created else "Machine updated successfully!"
        setattr(self.context['view'], 'success_message', success_message)
