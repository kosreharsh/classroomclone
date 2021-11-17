from typing import List
from django.core.checks import messages
from django.shortcuts import render, redirect
from .models import TodoTasks
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import TodoTasksSerializer
# Create your views here.


class TodoList(ListCreateAPIView):
    serializer_class = TodoTasksSerializer

    def get_queryset(self):
        user = self.request.user
        return TodoTasks.objects.filter(user=user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoTasksSerializer
    queryset = TodoTasks.objects.all()
