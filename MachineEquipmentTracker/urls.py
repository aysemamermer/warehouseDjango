from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('machines.urls')),
    path('api/', include('equipment.urls')),
]
