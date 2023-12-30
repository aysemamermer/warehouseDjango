from django.urls import path
from .views import MachineListCreateView, MachineDetailView, MachineDeleteView

urlpatterns = [
    path('machines/', MachineListCreateView.as_view(), name='machine-list-create'),
    path('machines/<int:pk>/', MachineDetailView.as_view(), name='machine-detail'),
    path('machines/<int:pk>/delete/', MachineDeleteView.as_view(), name='machine-delete'),
    # Diğer path'leri ekleyin
]
