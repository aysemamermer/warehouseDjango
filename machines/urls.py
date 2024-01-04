# urls.py
from .views import MachineViewSet, MachineDetailView, MachineDeleteView, MachineEquipmentListView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'machines', MachineViewSet, basename='machine')

urlpatterns = [
    path('machines/<int:pk>/', MachineDetailView.as_view(), name='machine-detail'),
    path('machines/<int:pk>/delete/', MachineDeleteView.as_view(), name='machine-delete'),
    path('machines/<int:pk>/equipments/', MachineEquipmentListView.as_view(), name='machine-equipments'),
    path('', include(router.urls)),
]
