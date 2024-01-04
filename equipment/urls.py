from .views import EquipmentViewSet, EquipmentDetailView, EquipmentDeleteView
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'equipment', EquipmentViewSet, basename='equipment')

urlpatterns = [
    path('', include(router.urls)),
    path('equipment/<int:pk>/delete/', EquipmentDeleteView.as_view(), name='equipment-delete'),
    path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),

]
