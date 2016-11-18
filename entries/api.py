from rest_framework import viewsets

from .models import Project, Entry, EntryType
from .serializers import ProjectSerializer, EntrySerializer, EntryTypeSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class EntryTypeViewSet(viewsets.ModelViewSet):
    queryset = EntryType.objects.all()
    serializer_class = EntryTypeSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
