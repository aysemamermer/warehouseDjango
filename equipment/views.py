from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Equipment
from .serializers import EquipmentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EquipmentListCreateView(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentDeleteView(APIView):
    def delete(self, request, pk):
        equipment = get_object_or_404(Equipment, pk=pk)
        # İzin kontrolü ve silme işlemi burada gerçekleştirilebilir
        equipment.delete()
        return Response({'message': 'Equipment deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


# views.py
class EquipmentView(APIView):
    def post(self, request, *args, **kwargs):
        # Burada ekipman ekleme işlemini gerçekleştirin
        # ...
        return Response({'message': 'Equipment added successfully'}, status=status.HTTP_201_CREATED)
