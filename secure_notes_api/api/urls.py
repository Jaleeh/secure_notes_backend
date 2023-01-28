
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet,SingleNoteView

router = DefaultRouter()
router.register(r'notes', NoteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('notes/<int:pk>/',SingleNoteView.as_view(),name = 'note'), #gets note by id



]