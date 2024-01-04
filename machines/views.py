from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Machine
from .serializers import MachineSerializer
from equipment.models import Equipment
from equipment.serializers import EquipmentSerializer
from rest_framework.exceptions import APIException


class MachineListCreateView(generics.ListCreateAPIView):
    """
    API endpoint that allows listing and creation of machines.
    """
    serializer_class = MachineSerializer

    def get_queryset(self):
        """Get the queryset for listing machines."""
        queryset = Machine.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        """
        Override the list method.
        """
        response = super().list(request, *args, **kwargs)
        return response

    def create(self, request, *args, **kwargs):
        """Override the create method to include a success message in the response."""
        response = super().create(request, *args, **kwargs)
        success_message = getattr(self, 'success_message', None)
        if success_message:
            response.data['success_message'] = success_message
        return response

    def update(self, request, *args, **kwargs):
        """Override the update method to include a success message in the response."""
        response = super().update(request, *args, **kwargs)
        success_message = getattr(self, 'success_message', None)
        if success_message:
            response.data['success_message'] = success_message
        return response


class MachineDeleteView(generics.DestroyAPIView):
    """
    API endpoint that allows deletion of a machine.
    """
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    def delete(self, request, *args, **kwargs):
        """Override the delete method to check for associated equipment and provide a success message."""
        instance = self.get_object()
        equipment_count = Equipment.objects.filter(machine=instance).count()

        if equipment_count > 0:
            raise APIException(detail='This machine is associated with equipment. You cannot delete it.',
                               code=status.HTTP_400_BAD_REQUEST)

        self.perform_destroy(instance)
        success_message = f"Machine {instance.name} deleted successfully."

        data = {'detail': success_message, 'success_message': success_message}
        return Response(data, status=status.HTTP_204_NO_CONTENT)


class MachineDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows retrieval, update, and deletion of a machine.
    """
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    def retrieve(self, request, *args, **kwargs):
        """Override the retrieve method to include equipment details in the response."""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        equipment_queryset = Equipment.objects.filter(machine=instance)
        equipment_serializer = EquipmentSerializer(equipment_queryset, many=True)
        data = {
            'machine_details': serializer.data,
            'equipment_list': equipment_serializer.data
        }
        return Response(data)


class MachineEquipmentListView(generics.ListAPIView):
    """
    API endpoint that allows listing of equipment associated with a specific machine.
    """
    serializer_class = EquipmentSerializer

    def get_queryset(self):
        """Get the queryset for listing equipment associated with a machine."""
        machine = get_object_or_404(Machine, pk=self.kwargs['pk'])
        return machine.equipment_set.all()
