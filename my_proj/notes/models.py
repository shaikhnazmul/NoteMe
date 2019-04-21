from django.db import models
from django.urls import reverse

class Note(models.Model):
    name = models.CharField(max_length=200)
    serial = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('note_edit', kwargs={'pk': self.pk})