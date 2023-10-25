from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task_list/',
        'Detail': '/task_detail/<str:pk>/',
        'Create': '/task_create/',
        'Update': '/task_update/<str:pk>/',
        'Delete': '/task_delete/<str:pk>/',

    }

    return Response(api_urls)


@api_view(['GET'])
def apiOverview1(request):
    api_urls = {
        'Register': '/api/register/',


    }

    return Response(api_urls)


@api_view(['GET'])
def Tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializers(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def TaskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializers(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateTask(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def UpdateTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def DeleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('successfully deleted')



