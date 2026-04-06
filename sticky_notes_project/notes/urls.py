from django.urls import path
from . import views

urlpatterns = [
    # Home page → list all notes
    path("", views.note_list, name="note_list"),

    # View a single note
    path("note/<int:pk>/", views.note_detail, name="note_detail"),

    # Create a new note
    path("note/new/", views.note_create, name="note_create"),

    # Update a note
    path("note/<int:pk>/edit/", views.note_update, name="note_update"),

    # Delete a note
    path("note/<int:pk>/delete/", views.note_delete, name="note_delete"),
]