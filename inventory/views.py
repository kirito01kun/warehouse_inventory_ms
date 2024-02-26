from django.shortcuts import render

def index(request):
    return render(request, 'inventory/index.html')

def about(request):
    return render(request, 'inventory/about.html')
