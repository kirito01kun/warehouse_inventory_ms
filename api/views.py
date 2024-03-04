from django.http import JsonResponse
from .models import RackInventory

def api_home(request):
    return JsonResponse({'message': 'Welcome to the API!'})

def api_about(request):
    return JsonResponse({'message': 'This is the about page of the API.'})


def inventory_list(request):
    levels = RackInventory.objects.all()

    # Format the data as JSON
    data = [{'rack_number': level.rack_number,
             'level_0': level.level_0,
             'level_1': level.level_1,
             'level_2': level.level_2,
             'level_3': level.level_3} for level in levels]

    return JsonResponse({'inventory': data})
