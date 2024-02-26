from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.api_home, name='api-home'),
    path('about/', views.api_about, name='api-about'),
]
