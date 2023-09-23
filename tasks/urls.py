from django.urls import path, include

from . import views

urlpatterns = [

    path('register', views.register),

    path('my-login', views.my_login),

    path('', views.home),

    #- CRUD operations

    #-CREATE TASK
    path('create-task', views.createTask, name='create-task'),

    #-READ TASK
    path('view-task', views.viewTasks, name='view-tasks'),

    #-UPDATE TASK
    path('update-task/<str:pk>/', views.updateTask, name='update-task'),

    #-DELETE TASK
    path('delete-task/<str:pk>/', views.deleteTask, name='delete-task'),
]