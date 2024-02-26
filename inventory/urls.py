from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='inventory-index'),
    path('about/', views.about, name='inventory-about'),
    
]