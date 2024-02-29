from django.http import JsonResponse
from .models import Person

def api_home(request):
    return JsonResponse({'message': 'Welcome to the API!'})

def api_about(request):
    return JsonResponse({'message': 'This is the about page of the API.'})

def api_home(request):
    personnes = Person.objects()[:5]
    data = [{'nom': p.nom, 'prenom': p.prenom, 'age': p.age, 'cp': p.cp} for p in personnes]
    return JsonResponse({'personnes': data})
