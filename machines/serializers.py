from .models import Machine
from rest_framework import serializers

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['id', 'name', 'inventory_number', 'location', 'description', 'created_at']

    def validate_inventory_number(self, value):
        if self.instance and self.instance.inventory_number == value:
            return value

        if Machine.objects.filter(inventory_number=value).exists():
            raise serializers.ValidationError("Another machine with this inventory number already exists.")

        return value

    def create(self, validated_data):
        instance = super().create(validated_data)
        self.add_success_message(instance, created=True)
        return instance

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        if Machine.objects.exclude(id=instance.id).filter(inventory_number=validated_data['inventory_number']).exists():
            raise serializers.ValidationError("Another machine with this inventory number already exists.")

        instance.save()
        self.add_success_message(instance, created=False)
        return instance

    def add_success_message(self, instance, created):
        success_message = "Machine created successfully!" if created else "Machine updated successfully!"
        setattr(self.context['view'], 'success_message', success_message)
