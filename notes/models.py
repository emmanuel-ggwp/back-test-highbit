from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)  # Title of the note
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp when the note is created
    updated_at = models.DateTimeField(
        auto_now=True
    )  # Timestamp when the note is last updated

    def __str__(self):
        return self.title
