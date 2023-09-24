from django.urls import path, include

from . import views

urlpatterns = [


#----------------------HomePage------------------------

path('', views.home, name=""),


#----------------------Dashboard------------------------
##----------------------------------------------------------## 

path('dashboard', views.dashboard, name='dashboard'),    

#----------------------Create a Task------------------------
##----------------------------------------------------------## 

path('create-task', views.createTask, name='create-task'),

#----------------------READ Task------------------------
##----------------------------------------------------------## 

path('view-tasks', views.viewTask, name='view-tasks'),

#----------------------UPDATE Task------------------------
##----------------------------------------------------------## 

path('update-task/<str:pk>/', views.updateTask, name='update-task'),

#----------------------DELETE Task------------------------
##----------------------------------------------------------##

path('delete-task/<str:pk>/', views.deleteTask, name='delete-task'),








#---------------------- Registration------------------------
##----------------------------------------------------------## 

path('register', views.register, name='register'),


#----------------------Login------------------------
##----------------------------------------------------------## 

path('my-login', views.my_login, name='my-login'),


#----------------------Logout------------------------
##----------------------------------------------------------##

path('user-logout', views.user_logout, name='user-logout'),

]