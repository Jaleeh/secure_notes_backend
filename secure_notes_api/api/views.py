
from rest_framework import viewsets,permissions,response,generics,status
from rest_framework.generics import RetrieveAPIView
from .models import Note
from .serializers import NoteSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import Http404


#view all notes
class NoteViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Note.objects.all() #gets all notes
    serializer_class = NoteSerializer

    def update(self,request,*args,**kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,partial = True )
        serializer.is_valid(raise_excepton = True)
        self.perform_update(serializer)
        return response.Response(serializer.data)
    
    def perform_create(self, serializer):
        return serializer.save(name=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return response.Response(status=status.HTTP_204_NO_CONTENT)
    
    def retrieve(self, request, pk = None):
        user = request.user
        try:
            note = Note.objects.get(pk=pk,name=user)
        except Note.DoesNotExist:
            raise Http404
        serializer = self.get_serializer(note)
        return response.Response(serializer.data)
        

# #view individual note
# class SingleNoteView(RetrieveAPIView):
#     authentication_classes = (JWTAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = NoteSerializer
#     def get_queryset(self):
#         return Note.objects.filter(id=self.kwargs.get(self.lookup_field))#filter based on ID

# class NoteDeleteView(generics.DestroyAPIView): 
#     authentication_classes = (JWTAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = Note.objects.all() 
#     serializer_class = NoteSerializer

#     def delete(self,request,pk):
#         try:
#             note = Note.objects.get(pk=pk,user = request.user) # check note exists in user account
#         except Note.DoesNotExist:
#             return response.Response(status= status.HTTP_404_NOT_FOUND)
#         note.delete() #if True then delete note
#         return response.Response(status= status.HTTP_204_NO_CONTENT) 


# class NoteCreateView(generics.CreateAPIView):
#     authentication_classes = (JWTAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

#     def perform_create(self, serializer):
#         return serializer.save(user=self.request.user)