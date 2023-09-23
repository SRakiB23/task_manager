from django.urls import path, include

from . import views

urlpatterns = [

    path('register', views.register),

    path('my-login', views.my_login),

    path('', views.home),
]