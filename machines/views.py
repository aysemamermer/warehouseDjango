from rest_framework import generics

from .serializers import MachineSerializer

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Machine

from rest_framework import generics
from .models import Machine
from .serializers import MachineSerializer
from rest_framework.response import Response
from rest_framework import status

class MachineListCreateView(generics.ListCreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class MachineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

# Diğer gerekli importları ekleyin

class MachineDeleteView(APIView):
    def delete(self, request, pk):
        machine = get_object_or_404(Machine, pk=pk)
        machine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
