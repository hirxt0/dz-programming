import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Starship

def ship_list(request):
    ships = Starship.objects.all()
    return render(request, 'ships/ship_list.html', {'ships': ships})

def ship_detail(request, pk):
    ship = Starship.objects.get(pk=pk)
    return render(request, 'ships/ship_detail.html', {'ship': ship})

def fetch_ships_from_api(request):
    url = "https://swapi.dev/api/starships/"
    
    try:
        while url:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            for ship_data in data['results']:
                Starship.objects.update_or_create(
                    url=ship_data['url'],
                    defaults={
                        'name': ship_data['name'],
                        'model': ship_data['model'],
                        'manufacturer': ship_data['manufacturer'],
                        'cost_in_credits': ship_data['cost_in_credits'],
                        'length': ship_data['length'],
                        'max_atmosphering_speed': ship_data['max_atmosphering_speed'],
                        'crew': ship_data['crew'],
                        'passengers': ship_data['passengers'],
                        'cargo_capacity': ship_data['cargo_capacity'],
                        'starship_class': ship_data['starship_class'],
                    }
                )
            
            url = data['next']
        
        messages.success(request, 'Корабли успешно загружены!')
    except requests.RequestException as e:
        messages.error(request, f'Ошибка при загрузке: {e}')
    
    return redirect('ship_list')

def search_ships(request):
    query = request.GET.get('q', '')
    ships = Starship.objects.filter(name__icontains=query) if query else []
    return render(request, 'ships/search.html', {'ships': ships, 'query': query})