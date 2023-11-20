from django.shortcuts import render
from django.http import JsonResponse

from .models import Task

from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import TaskSerializer

# Create your views here.

@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List':'/task-list',
        'Detail':'/task-detail/<str:pk>/',
        'Update':'/task-update/<str:pk>/',
        'Create':'/task-create',
        'Delete':'/task-delect/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)
