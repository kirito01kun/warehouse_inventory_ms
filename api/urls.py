from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.inventory_list, name='inventory-list'),
    path('inventory/<str:pk>/', views.inventory_detail, name='inventory-detail'),
    path('create/', views.inventory_create, name='inventory-create'),
    path('update/<str:pk>/', views.inventory_update, name='inventory-update'),
    path('delete/<str:pk>/', views.inventory_delete, name='inventory-delete'),
]
