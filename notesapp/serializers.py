from rest_framework import serializers
from .models import Note, SharedNote

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'type']

class SharedNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedNote
        fields = ['id', 'note', 'shared_with']
