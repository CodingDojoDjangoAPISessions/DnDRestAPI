from django.shortcuts import render
from characters.models import Character


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    all_the_characters = Character.objects.all()
    context = {
        'all_the_characters': all_the_characters # queryset
    }
    return render(request, 'dashboard.html', context)
