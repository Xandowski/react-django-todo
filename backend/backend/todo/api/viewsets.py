from backend.todo.api.serializers import TodoSerializer
from backend.todo.models import Todo
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
