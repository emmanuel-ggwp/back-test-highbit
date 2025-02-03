from django.db import models

from status.models import Status


class Note(models.Model):
    title = models.CharField(
        max_length=200, blank=False, null=False
    )  # Title of the note
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp when the note is created
    updated_at = models.DateTimeField(
        auto_now=True
    )  # Timestamp when the note is last updated
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ["-updated_at"]

    def save(self, *args, **kwargs):
        if not self.status_id:
            self.status = Status.objects.get(id=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
