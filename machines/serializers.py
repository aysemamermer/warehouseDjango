from .models import Machine
from rest_framework import serializers


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['id', 'name', 'inventory_number', 'location', 'description', 'created_at']

    def create(self, validated_data):
        instance = super().create(validated_data)
        self.add_success_message(instance, created=True)
        return instance

    def update(self, instance, validated_data):
        instance.__dict__.update(validated_data)
        instance.save()

        if Machine.objects.exclude(id=instance.id).filter(inventory_number=validated_data['inventory_number']).exists():
            raise serializers.ValidationError("Inventory number already exists.")

        self.add_success_message(instance, created=False)
        return instance

    def add_success_message(self,instance ,created):
        success_message = "Machine created successfully!" if created else "Machine updated successfully!"
        setattr(self.context['view'], 'success_message', success_message)
