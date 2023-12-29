from django.urls import path
from .views import MachineListCreateView, MachineDetailView

urlpatterns = [
    path('machines/', MachineListCreateView.as_view(), name='machine-list-create'),
    path('machines/<int:pk>/', MachineDetailView.as_view(), name='machine-detail'),
]
