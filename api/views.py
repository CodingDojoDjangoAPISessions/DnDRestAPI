from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CharacterSerializer
from characters.models import Character

# Create your views here.

class CharacterViewSetResponses(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()