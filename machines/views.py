# views.py
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Machine
from .serializers import MachineSerializer
from equipment.models import Equipment
from equipment.serializers import EquipmentSerializer

class MachineListCreateView(generics.ListCreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

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
        self.perform_destroy(instance)
        return Response({'detail': 'Machine deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
