# views.py
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Machine
from .serializers import MachineSerializer
from equipment.models import Equipment
from equipment.serializers import EquipmentSerializer
from .filters import MachineFilter
from rest_framework.exceptions import APIException


class MachineListCreateView(generics.ListCreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    filterset_class = MachineFilter

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        success_message = getattr(self, 'success_message', None)
        if success_message:
            response.data['success_message'] = success_message
        return response

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        success_message = getattr(self, 'success_message', None)
        if success_message:
            response.data['success_message'] = success_message
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        success_message = getattr(self, 'success_message', None)
        if success_message:
            response.data['success_message'] = success_message
        return response


class MachineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    def retrieve(self, request, *args, **kwargs):
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
    serializer_class = EquipmentSerializer

    def get_queryset(self):
        machine = get_object_or_404(Machine, pk=self.kwargs['pk'])
        return machine.equipment_set.all()


class MachineDeleteView(generics.DestroyAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        equipment_count = Equipment.objects.filter(machine=instance).count()

        if equipment_count > 0:
            raise APIException(detail='This machine is associated with equipment. You cannot delete it.',
                               code=status.HTTP_400_BAD_REQUEST)

        self.perform_destroy(instance)
        success_message = f"Machine {instance.name} deleted successfully."
        setattr(self, 'success_message', success_message)
        return Response({'detail': success_message}, status=status.HTTP_204_NO_CONTENT)
