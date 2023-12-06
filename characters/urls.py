from django.urls import path  # Import path function from django.urls to define URL patterns
from . import views  # Import views from the current directory (i.e., from the same app)

urlpatterns = [
    # URL pattern for the first_view. When the 'hello/' URL is accessed, first_view from views.py will be called.
    path('hello/', views.first_view),

    # URL pattern for create_character view. 'create/' URL will call create_character view. 
    # The name='create_character' allows you to refer to this URL pattern by name elsewhere in your Django project.
    path('create/', views.create_character, name='create_character'),

    # URL pattern for post_char view. 'created/' URL will call post_char view. 
    # The name='post_char' provides a convenient name to refer to this URL.
    path('created/', views.post_char, name='post_char'),

    # URL pattern for view_character view with a dynamic segment '<int:char_id>'. 
    # This pattern will match any URL like 'view/1/', 'view/2/', etc., 
    # and the value of char_id will be passed as an integer argument to the view_character view.
    path('view/<int:char_id>/', views.view_character, name='view_character'),

    # URL pattern for edit_character view. Similar to view_character, 
    # it uses a dynamic URL segment to pass the character ID to the edit_character view.
    path('edit/<int:char_id>/', views.edit_character, name='edit_character'),

    # URL pattern for update_character view. It uses a dynamic segment to pass the character ID 
    # and will call update_character view when a URL like 'update/1/' is accessed.
    path('update/<int:char_id>/', views.update_character, name='update_character'),

    # URL pattern for delete_character view. Similar to the above patterns, 
    # it uses '<int:char_id>' to dynamically capture and pass the character ID to the delete_character view.
    path('delete/<int:char_id>/', views.delete_character, name='delete_character')
]
