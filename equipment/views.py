from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from machines.serializers import MachineSerializer
from .models import Equipment
from .serializers import EquipmentSerializer


class EquipmentListCreateView(generics.ListCreateAPIView):
    serializer_class = EquipmentSerializer

    def get_queryset(self):
        """Retrieve all equipment objects"""
        queryset = Equipment.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        """Override the list method to include success_message in the response"""
        response = super().list(request, *args, **kwargs)
        success_message = getattr(self, 'success_message', None)
        if success_message:
            response.data['success_message'] = success_message
        return response

    def create(self, request, *args, **kwargs):
        """"Override the create method to include success_message in the response"""
        response = super().create(request, *args, **kwargs)
        success_message = getattr(self, 'success_message', None)
        if success_message:
            response.data['success_message'] = success_message
        return response


class EquipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def update(self, request, *args, **kwargs):
        """Override the update method to include success_message in the response"""
        response = super().update(request, *args, **kwargs)
        success_message = getattr(self, 'success_message', None)
        if success_message:
            response.data['success_message'] = success_message
        return response


class EquipmentDeleteView(APIView):
    def delete(self, request, pk):
        """"Retrieve the equipment object and delete it"""
        equipment = get_object_or_404(Equipment, pk=pk)
        equipment.delete()
        success_message = 'Equipment deleted successfully.'
        data = {'message': success_message, 'success_message': success_message}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
