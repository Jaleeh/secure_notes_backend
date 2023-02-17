
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import NoteViewSet,SingleNoteView,NoteDeleteView,NoteCreateView
from .views import NoteViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET','POST'])
def my_notes(request):
    notes = Note.objects.filter(name=request.user.id)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

router = DefaultRouter()
router.register(r'notes', NoteViewSet,basename = 'note')

urlpatterns = [
    path('', include(router.urls)),
    # path('notes/<int:pk>/',SingleNoteView.as_view(),name = 'note'), #gets note by id
    # path('notes/<int:pk>/delete',NoteDeleteView.as_view(),name = 'delete_note'), #deletes note by id
    # path('notes/create', NoteCreateView.as_view(), name='note-create'),
    
    path('notes/<int:pk>/', NoteViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy','post': 'perform_create'}), name='single-note'),
    path('mynotes/',my_notes),
    

]
urlpatterns+=router.urls