from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='warehouse-index'),
    path('about/', views.about, name='warehouse-about'),
    
]
