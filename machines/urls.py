# urls.py
from django.urls import path
from .views import MachineListCreateView, MachineDetailView, MachineDeleteView, MachineEquipmentListView

urlpatterns = [
    path('machines/', MachineListCreateView.as_view(), name='machine-list-create'),
    path('machines/<int:pk>/', MachineDetailView.as_view(), name='machine-detail'),
    path('machines/<int:pk>/delete/', MachineDeleteView.as_view(), name='machine-delete'),
    path('machines/<int:pk>/equipments/', MachineEquipmentListView.as_view(), name='machine-equipments'),
]
