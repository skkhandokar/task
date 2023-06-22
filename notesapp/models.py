from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Note(models.Model):
    TYPE_CHOICES = (
        ('text', 'Text'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class SharedNote(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.note.title} - Shared with: {self.shared_with.username}'
