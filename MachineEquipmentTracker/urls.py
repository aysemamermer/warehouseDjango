from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-machines/', include('machines.urls')),
    path('api-equipment/', include('equipment.urls')),
]
