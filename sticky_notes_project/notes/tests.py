from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteModelTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note."
        )

    def test_note_title(self):
        self.assertEqual(self.note.title, "Test Note")

    def test_note_content(self):
        self.assertEqual(self.note.content, "This is a test note.")

    def test_string_representation(self):
        self.assertEqual(str(self.note), "Test Note")

    def test_note_ordering(self):
        older_note = Note.objects.create(
            title="Older Note",
            content="Older content"
        )
        newer_note = Note.objects.create(
            title="Newer Note",
            content="Newer content"
        )
        notes = list(Note.objects.all())
        self.assertEqual(notes[0], newer_note)
        self.assertIn(older_note, notes)


class NoteViewTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note."
        )

    def test_note_list_view(self):
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertContains(response, "This is a test note.")

    def test_note_detail_view(self):
        response = self.client.get(reverse("note_detail", args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertContains(response, "This is a test note.")

    def test_note_create_view(self):
        response = self.client.post(reverse("note_create"), {
            "title": "New Note",
            "content": "New content"
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 2)
        self.assertEqual(Note.objects.first().title, "New Note")
        self.assertEqual(Note.objects.first().content, "New content")

    def test_note_update_view(self):
        response = self.client.post(reverse("note_update", args=[self.note.id]), {
            "title": "Updated Note",
            "content": "Updated content"
        })
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Note")
        self.assertEqual(self.note.content, "Updated content")

    def test_note_delete_view(self):
        response = self.client.post(reverse("note_delete", args=[self.note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 0)

    def test_note_detail_view_404_for_invalid_note(self):
        response = self.client.get(reverse("note_detail", args=[999]))
        self.assertEqual(response.status_code, 404)