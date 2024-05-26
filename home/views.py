from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Film


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('/about')
    
def search_film_name(request):
    title = request.GET.get('french_title')
    payload = []
    if title:
        film_objs = Film.objects.filter(french_title__icontains=title)

        for film_obj in film_objs:
            payload.append(f'{film_obj.french_title} ({film_obj.release_year})')
    
    return JsonResponse({'status' : 200, 'data' : payload})