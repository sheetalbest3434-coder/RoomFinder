from django.shortcuts import render
from .models import Room

def home(request):
    query = request.GET.get('q')  # search input
    if query:
        rooms = Room.objects.filter(location__icontains=query)
    else:
        rooms = Room.objects.all()

    return render(request, 'main/home.html', {'rooms': rooms})
