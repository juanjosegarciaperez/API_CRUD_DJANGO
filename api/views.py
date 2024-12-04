from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import programmer

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = ProgrammerSerializer
    