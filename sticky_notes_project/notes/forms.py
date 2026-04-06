from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """
    Form for creating and updating notes.
    """

    class Meta:
        model = Note
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter note title",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write your note here...",
                    "rows": 8,
                }
            ),
        }