from rest_framework import viewsets
from todoapp.models import ToDoList
from todoapp.serializers import DeloSerializer

class DeloViewSet(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = DeloSerializer