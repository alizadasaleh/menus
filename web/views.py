from django.shortcuts import render

from web.models import MenuItem


def index(request):
    
    return render(request, 'index.html')

def menus(request):
    menus = MenuItem.objects.values_list('menu_name', flat=True).distinct()
    return render(request, 'menus.html', {'menus': menus})
