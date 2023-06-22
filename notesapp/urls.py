

from django.urls import path
from   .views import NoteListCreateView, NoteRetrieveUpdateDeleteView, ShareNoteView, UserNotesView

urlpatterns = [
    path('api/notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('api/notes/<int:pk>/', NoteRetrieveUpdateDeleteView.as_view(), name='note-retrieve-update-delete'),
    path('api/notes/<int:pk>/share/', ShareNoteView.as_view(), name='share-note'),
    path('api/users/<str:username>/notes/', UserNotesView.as_view(), name='user-notes'),
]
