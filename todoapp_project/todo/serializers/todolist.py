from rest_framework import serializers
from .model import TodoList




class TodolListSerializer(serializers.ModelSerializers)
class Meta:
    model = TodolList 
    fields ='__all__'
