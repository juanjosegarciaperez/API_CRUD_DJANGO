from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .serializer import StudentSerializer
from .models import programmer
from .models import student

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = ProgrammerSerializer
    
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudentSerializer