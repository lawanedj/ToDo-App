from rest_framework import serializers
from .model import Todo, TodolList 


class TodoSerializer(serializers.ModelSerializers)
class Meta:
    model = Todo 
    fields ='__all__'



class TodolListSerializer(serializers.ModelSerializers)
class Meta:
    model = TodolList 
    fields ='__all__'


