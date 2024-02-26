from django.http import JsonResponse

def api_home(request):
    return JsonResponse({'message': 'Welcome to the API!'})

def api_about(request):
    return JsonResponse({'message': 'This is the about page of the API.'})
