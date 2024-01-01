from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Equipment
from .serializers import EquipmentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

class EquipmentDeleteView(APIView):
    def delete(self, request, pk):
        equipment = get_object_or_404(Equipment, pk=pk)
        equipment.delete()
        return Response({'message': 'Equipment deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

class EquipmentCreateView(APIView):
    def post(self, request, *args, **kwargs):
        # Burada eklenecek ekipmanın verilerini request'ten alın ve serializer kullanarak kaydedin.
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Equipment added successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
