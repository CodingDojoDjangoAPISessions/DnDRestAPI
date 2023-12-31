from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Character  # Import the Character model from the current app's models.py
from .fithed_srd_connection import get_all_classes
from users import views  # Import views from the 'users' app (if exists)
import os


def first_view(request):
    return HttpResponse('Hello Ninjas!')  # Returns a simple HTTP response saying "Hello Ninjas!"


def create_character(request):
    classes = get_all_classes()
    class_options =[]
    for c in classes:
        class_options.append({"name": c["name"], "index": c["index"]})
    # print(request.__dict__)
    print(class_options)
    return render(request, 'create_character.html', context={"class_options": class_options})  # Renders the create_character.html template


def post_char(request):
    print("Here is the POST data:")
    print(request.POST)
    if request.method == 'POST':  # Check if the request method is POST
        character_data = {
            'name': request.POST.get('name'),  # Retrieves the 'name' value from POST data
            'char_class': request.POST.get('char_class'),  # Retrieves the 'char_class' value from POST data
            'level': request.POST.get('level'),  # ...similarly for other fields
            'exp': request.POST.get('exp'),
            'str_stat': request.POST.get('str_stat'),
            'dex_stat': request.POST.get('dex_stat'),
            'con_stat': request.POST.get('con_stat'),
            'int_stat': request.POST.get('int_stat'),
            'wis_stat': request.POST.get('wis_stat'),
            'cha_stat': request.POST.get('cha_stat'),
            'background': request.POST.get('background')
        }
        request.session['character_data'] = character_data  # Store the character data in session
        new_char = Character.objects.create(**character_data)  # Create a new Character instance with the POST data
        return redirect('dashboard')  # Redirect to the 'dashboard' view
    return render(request, 'dashboard')  # If not a POST request, render the dashboard template


def view_character(request, char_id):
    character = Character.objects.get(id=char_id)  # Retrieve the Character instance with the given char_id
    context = {
        "character": character  # Context variable 'character' to pass to the template
    }
    return render(request, 'view_character.html', context)  # Render the view_character.html template with the context


def edit_character(request, char_id):
    character = Character.objects.get(id=char_id)  # Retrieve the Character instance with the given char_id
    context = {
        "character": character  # Context variable 'character' to pass to the template
    }
    return render(request, 'edit_character.html', context)  # Render the edit_character.html template with the context


def update_character(request, char_id):
    if request.method == 'POST':  # Check if the request method is POST
        character_data = {
            # Retrieves values from POST data similar to post_char function
            'name': request.POST.get('name'),
            # ...
            'background': request.POST.get('background')
        }
        character = Character.objects.get(id=char_id)  # Retrieve the Character instance with the given char_id
        for key, value in character_data.items():
            setattr(character, key, value)  # Update each field of the character with new values
        character.save()  # Save the changes to the character in the database
        return redirect('dashboard')  # Redirect to the 'dashboard' view
    else:
        pass  # No action for non-POST requests


def delete_character(request, char_id):
    character = Character.objects.get(id=char_id)  # Retrieve the Character instance with the given char_id
    character.delete()  # Delete the retrieved character
    return redirect('dashboard')  # Redirect to the dashboard view
