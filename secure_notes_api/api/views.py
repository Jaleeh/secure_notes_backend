
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from .models import Note
from .serializers import NoteSerializer

#view all notes
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

#view individual note
class SingleNoteView(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'id'
