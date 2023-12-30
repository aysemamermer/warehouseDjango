from django.urls import path
from .views import EquipmentListCreateView, EquipmentDetailView, EquipmentDeleteView

urlpatterns = [
    path('equipment/', EquipmentListCreateView.as_view(), name='equipment-list-create'),
    path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),
    path('equipment/<int:pk>/delete/', EquipmentDeleteView.as_view(), name='equipment-delete'),
    # Silme işlemi için eklenen satır
]
