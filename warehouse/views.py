# warehouse/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'warehouse/index.html')


def about(request):
    return render(request, 'warehouse/about.html')
