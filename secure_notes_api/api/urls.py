
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet,SingleNoteView,NoteDeleteView,NoteCreateView


router = DefaultRouter()
router.register(r'notes', NoteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('notes/<int:pk>/',SingleNoteView.as_view(),name = 'note'), #gets note by id
    path('notes/<int:pk>/',NoteDeleteView.as_view(),name = 'delete_note'), #deletes note by id
    path('notes/create', NoteCreateView.as_view(), name='note-create'),



]