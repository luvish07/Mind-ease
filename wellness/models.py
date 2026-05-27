from django.db import models


class GratitudeEntry(models.Model):
    text = models.CharField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "gratitude entries"

    def __str__(self):
        return self.text
