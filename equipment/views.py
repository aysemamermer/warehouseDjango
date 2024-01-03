# equipments/views.py
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Equipment
from .serializers import EquipmentSerializer
from machines.serializers import MachineSerializer
from .filters import EquipmentFilter


class EquipmentListCreateView(generics.ListCreateAPIView):
    serializer_class = EquipmentSerializer
    filterset_class = EquipmentFilter

    def get_queryset(self):
        queryset = Equipment.objects.all()
        return queryset


class EquipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        machine_serializer = MachineSerializer(instance.machine)  # Serialize the machine instance
        data = {
            'equipment_details': serializer.data,
            'machine_details': machine_serializer.data  # Include serialized machine details
        }
        return Response(data)


class EquipmentDeleteView(APIView):
    def delete(self, request, pk):
        equipment = get_object_or_404(Equipment, pk=pk)
        equipment.delete()
        return Response({'message': 'Equipment deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class EquipmentCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Equipment added successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
