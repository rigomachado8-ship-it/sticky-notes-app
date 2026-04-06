from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note


def note_list(request):
    """
    Display all notes on the home page.
    """
    notes = Note.objects.all()

    context = {
        "notes": notes,
        "page_title": "All Sticky Notes",
    }
    return render(request, "notes/note_list.html", context)


def note_detail(request, pk):
    """
    Display the details of a single note.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    """
    Create a new note.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()

    context = {
        "form": form,
        "page_title": "Create Note",
        "button_text": "Save Note",
    }
    return render(request, "notes/note_form.html", context)


def note_update(request, pk):
    """
    Update an existing note.
    """
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_detail", pk=note.pk)
    else:
        form = NoteForm(instance=note)

    context = {
        "form": form,
        "page_title": "Edit Note",
        "button_text": "Update Note",
    }
    return render(request, "notes/note_form.html", context)


def note_delete(request, pk):
    """
    Delete an existing note after confirmation.
    """
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.delete()
        return redirect("note_list")

    return render(request, "notes/note_confirm_delete.html", {"note": note})