
from rest_framework import viewsets,permissions,response,generics
from rest_framework.generics import RetrieveAPIView
from .models import Note
from .serializers import NoteSerializer


#view all notes
class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Note.objects.all() #gets all notes
    serializer_class = NoteSerializer

    def update(self,request,*args,**kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,partial = True )
        serializer.is_valid(raise_excepton = True)
        self.perform_update(serializer)
        return response.Response(serializer.data)

#view individual note
class SingleNoteView(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NoteSerializer
    def get_queryset(self):
        return Note.objects.filter(id=self.kwargs.get(self.lookup_field))#filter based on ID

class NoteDeleteView(generics.DestroyAPIView): 
    queryset = Note.objects.all() 
    serializer_class = NoteSerializer
