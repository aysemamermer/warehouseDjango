from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from machines.serializers import MachineSerializer
from .models import Equipment
from .serializers import EquipmentSerializer
from rest_framework import viewsets
from django.db.models import Q
from .models import Equipment
from .serializers import EquipmentSerializer
from machines.models import Machine

class EquipmentViewSet(viewsets.ModelViewSet):
    serializer_class = EquipmentSerializer

    def get_queryset(self):
        queryset = Equipment.objects.all()
        #filter
        search_param = self.request.query_params.get('search', None)
        if search_param:
            queryset = queryset.filter(
                Q(name__icontains=search_param) |
                Q(inventory_number__icontains=search_param)
            )

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

    def update(self, request, *args, **kwargs):
        """Override the update method to include success_message in the response"""
        response = super().update(request, *args, **kwargs)
        success_message = getattr(self, 'success_message', None)
        if success_message:
            response.data['success_message'] = success_message
        return response

class EquipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Specify the queryset and serializer class for the view"""
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer





class EquipmentDeleteView(APIView):
    def delete(self, request, pk):
        """"Retrieve the equipment object and delete it"""
        equipment = get_object_or_404(Equipment, pk=pk)
        equipment.delete()
        success_message = 'Equipment deleted successfully.'
        data = {'message': success_message, 'success_message': success_message}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
