from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Note, SharedNote
from .serializers import NoteSerializer, SharedNoteSerializer

class NoteListCreateView(APIView):
    def get(self, request):
        notes = Note.objects.filter(user=request.user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk, user=request.user)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def put(self, request, pk):
        note = get_object_or_404(Note, pk=pk, user=request.user)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        note = get_object_or_404(Note, pk=pk, user=request.user)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ShareNoteView(APIView):
    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk, user=request.user)
        username = request.data.get('username')
        user = get_object_or_404(User, username=username)
        shared_note = SharedNote.objects.create(note=note, shared_with=user)
        serializer = SharedNoteSerializer(shared_note)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserNotesView(APIView):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        shared_notes = SharedNote.objects.filter(shared_with=user)
        serializer = SharedNoteSerializer(shared_notes, many=True)
        return Response(serializer.data)

