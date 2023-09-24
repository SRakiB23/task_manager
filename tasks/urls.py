from django.urls import path, include

from . import views

urlpatterns = [


#----------------------HomePage------------------------

path('', views.home, name=""),


#----------------------Dashboard------------------------
##----------------------------------------------------------## 

path('dashboard', views.dashboard, name='dashboard'),    



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