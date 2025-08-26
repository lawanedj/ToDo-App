from rest_framework import serializers
from .model import Todo


class TodoSerializer(serializers.ModelSerializers)
class Meta:
    model = Todo 
    fields ='__all__'


