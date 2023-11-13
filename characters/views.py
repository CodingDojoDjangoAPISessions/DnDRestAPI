from django.shortcuts import render
from django.http import HttpResponse

def first_view(request):
    return HttpResponse('Hello Ninjas!')

def create_character(request):
    print(request.__dict__)
    return render(request, 'create_character.html')