
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warehouse/', include('warehouse.urls')),
    path('inventory/', include('inventory.urls')),
    path('api/', include('api.urls')),
]
