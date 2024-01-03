# equipment/views.py
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from machines.serializers import MachineSerializer
from .models import Equipment
from .serializers import EquipmentSerializer
from .filters import EquipmentFilter


class EquipmentListCreateView(generics.ListCreateAPIView):
    serializer_class = EquipmentSerializer
    filterset_class = EquipmentFilter

    def get_queryset(self):
        queryset = Equipment.objects.all()
        return queryset

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

class EquipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        machine_serializer = MachineSerializer(instance.machine) if instance.machine else None
        data = {
            'equipment_details': serializer.data,
            'machine_details': machine_serializer.data if machine_serializer else None
        }
        return Response(data)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        success_message = getattr(self, 'success_message', None)
        if success_message:
            response.data['success_message'] = success_message
        return response


class EquipmentDeleteView(APIView):
    def delete(self, request, pk):
        equipment = get_object_or_404(Equipment, pk=pk)
        equipment.delete()
        success_message = 'Equipment deleted successfully.'
        data = {'message': success_message, 'success_message': success_message}
        return Response(data, status=status.HTTP_204_NO_CONTENT)

