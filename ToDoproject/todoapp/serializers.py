from rest_framework import serializers
from todoapp.models import ToDoList
class DeloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['id','delo']