from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiview'),
    path('register/', views.apiOverview1, name='apiview1'),
    path('task_list/', views.Tasklist, name='tasklist'),
    path('task_detail/<str:pk>/', views.TaskDetail, name='task_detail'),
    path('task_create/', views.CreateTask, name='Create'),
    path('task_update/<str:pk>/', views.UpdateTask, name='Update'),
    path('task_delete/<str:pk>/', views.DeleteTask, name='delete_task')

]